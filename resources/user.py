from flask_restful import Resource, request
from flask import request
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt,
)
from models.user import UserModel
from schemas.user import UserSchema
from models.clinical_story.clinical_story import ClinicalStoryModel
from schemas.clinical_story.clinical_story import ClinicalStorySchema
from blacklist import BLACKLIST
from utils.custom_errors import ResourceAlreadyExists, ResourceNotFound, InvalidCredentials, NotAuthorized
from utils.table_joiners import get_types_data
from datetime import datetime
import os

user_schema = UserSchema()
user_schema_list = UserSchema(many=True)

clinical_story_schema_list = ClinicalStorySchema(many=True)

from models.clinical_story.medicine import MedicineModel
from schemas.clinical_story.medicine import MedicineSchema
medicine_schema_list = MedicineSchema(many=True)

from models.clinical_story.symptom import SymptomModel
from schemas.clinical_story.symptom import SymptomSchema
symptom_schema_list = SymptomSchema(many=True)

from models.clinical_story.metadata import MetadataModel
from schemas.clinical_story.metadata import MetadataSchema
metadata_schema_list = MetadataSchema(many=True)

USER_DELETED = "Usuario eliminado"
USER_LOGGED_OUT = "Usuario <id={}> desconectado satisfactoriamente"

class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)
        print(user)
        if UserModel.find_by_email(user.email):
            raise ResourceAlreadyExists("error", { "email": ["Ya existe un recurso con este campo"]})

        if UserModel.find_by_username(user.username):
            raise ResourceAlreadyExists("error", { "username": ["Ya existe un recurso con este campo"]})

        if UserModel.find_by_document(user.document):
            raise ResourceAlreadyExists("error", { "document": ["Ya existe un recurso con este campo"]})

        user.password = generate_password_hash(user.password, method='sha256')
        user.save_to_db()

        return {"success": True, "data": user_schema.dump(user)}, 201

class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()

        user = UserModel.find_by_email(user_json['email'])

        if not user:
            raise ResourceNotFound

        if user.active == 0:
            raise ResourceNotFound

        if user and check_password_hash(user.password, user_json['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"success": True, "access_token": access_token, "refresh_token": refresh_token, "user": user_schema.dump(user)}, 200
            
        raise InvalidCredentials

class UserLogout(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        user_id = get_jwt_identity()
        BLACKLIST.add(jti)
        return {"success": True, "message": USER_LOGGED_OUT.format(user_id)}, 200

class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            raise ResourceNotFound

        user = user_schema.dump(user)

        clinical_stories = ClinicalStoryModel.find_by_user_id(user['id'])
        clinical_stories = clinical_story_schema_list.dump(clinical_stories)

        types = get_types_data(["medicine_types", "symptom_types", "metadata_types"])

        for clc_story in clinical_stories:
            c_id = clc_story["id"]

            medicines = MedicineModel.find_by_story_id(c_id)
            medicines = medicine_schema_list.dump(medicines)
            med_ids = [med["medicine_type_id"] for med in medicines]
            clc_medicines = []
            for med in types["medicine_types"]:
                if med["id"] in med_ids:
                    clc_medicines.append({ "id": med["id"], "nombre": med["nombre"], "principio_activo": med["principio_activo"], "presentacion": med["presentacion"] })
            
            symptoms = SymptomModel.find_by_story_id(c_id)
            symptoms = symptom_schema_list.dump(symptoms)
            symp_ids = [symp["symptom_type_id"] for symp in symptoms]
            clc_symptoms = []
            for symp in types["symptom_types"]:
                if symp["id"] in symp_ids:
                    clc_symptoms.append({ "id": symp["id"], "name": symp["name"], "description": symp["description"] })
            
            metadata = MetadataModel.find_by_story_id(c_id)
            metadata = metadata_schema_list.dump(metadata)
            metadata_ids = [metadata["metadata_type_id"] for metadata in metadata]
            clc_metadata = []
            for metadata in types["metadata_types"]:
                if metadata["id"] in metadata_ids:
                    clc_metadata.append({ "id": metadata["id"], "name": metadata["name"], "description": metadata["description"] })

            clc_story["medicines"] = clc_medicines
            clc_story["symptoms"] = clc_symptoms
            clc_story["metadata"] = clc_metadata

        user['clinical_stories'] = clinical_stories
        
        return { "success": True, "data": user }, 200

    @classmethod
    @jwt_required
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            raise ResourceNotFound

        requester_id = get_jwt_identity()

        print(requester_id != 1)
        if requester_id != user_id and requester_id != 1:
            raise NotAuthorized

        user.deactivate()
        return { "success": True, "data": {} }, 200

    @classmethod
    @jwt_required
    def put(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            raise ResourceNotFound

        requester_id = get_jwt_identity()

        print(user_id != 1)

        if requester_id != user_id and requester_id != 1:
            raise NotAuthorized

        fields_json = request.get_json()
        supported_fields = ['first_name', 'last_name', 'role', 'active']
        update_fields = { k : v for k, v in fields_json.items() if k in supported_fields}
        user.update(update_fields)
        return { "success": True, "data": user_schema.dump(user) }, 200

class Users(Resource):
    @classmethod
    @jwt_required
    def get(cls):
        query_params = request.args
        users = UserModel.get_list(query_params)
    
        return { "success": True, "data": user_schema_list.dump(users) }, 200

class UserImageUpload(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        str_time = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]
        f = request.files['image']
        f_name = str_time + secure_filename(f.filename)
        file_name = os.path.join("./static/" + f_name)
        f.save(file_name)


        user_id = get_jwt_identity()
        user = UserModel.find_by_id(user_id)

        user.img_url = f_name

        user.save_to_db()
        
        return { "success": True, "data": file_name }, 200 
