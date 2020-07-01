from flask_restful import Resource, request
from flask import request
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

user_schema = UserSchema()
user_schema_list = UserSchema(many=True)

clinical_story_schema_list = ClinicalStorySchema(many=True)

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

        user['clinical_stories'] = clinical_story_schema_list.dump(clinical_stories)
        
        return { "success": True, "data": user }, 200

    @classmethod
    @jwt_required
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            raise ResourceNotFound

        if user_id != get_jwt_identity():
            raise NotAuthorized

        user.deactivate()
        return { "success": True, "data": {} }, 200

    @classmethod
    @jwt_required
    def put(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            raise ResourceNotFound

        if user_id != get_jwt_identity():
            raise NotAuthorized

        fields_json = request.get_json()
        supported_fields = ['first_name', 'last_name', 'birth_date', 'work_city']
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