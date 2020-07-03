from flask_restful import Resource, request
from flask import request
from werkzeug.security import safe_str_cmp
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_jwt_extended import jwt_required, fresh_jwt_required, get_jwt_identity
   
from models.pacient.pacient import PacientModel
from schemas.pacient.pacient import PacientSchema

from models.pacient.personal_background import PersonalBackgroundModel
from schemas.pacient.personal_background import PersonalBackgroundSchema

from models.pacient.family_background import FamilyBackgroundModel
from schemas.pacient.family_background import FamilyBackgroundSchema

from models.pacient.profession_history import ProfessionHistoryModel
from schemas.pacient.profession_history import ProfessionHistorySchema

from models.pacient.allergy import AllergyModel
from schemas.pacient.allergy import AllergySchema

from models.pacient.vaccine import VaccineModel
from schemas.pacient.vaccine import VaccineSchema

from models.clinical_story.clinical_story import ClinicalStoryModel
from schemas.clinical_story.clinical_story import ClinicalStorySchema

from models.direction.direction import DirectionModel
from schemas.direction.direction import DirectionSchema

from models.direction.direction import MunicipalityModel
from schemas.direction.municipality import MunicipalitySchema

from models.direction.direction import StateModel
from schemas.direction.state import StateSchema

from models.direction.direction import CountryModel
from schemas.direction.country import CountrySchema

from utils.custom_errors import ResourceAlreadyExists, NotAuthorized, ResourceNotFound

pacient_schema = PacientSchema()
pacient_list_schema = PacientSchema(many=True)

clinical_story_schema_list = ClinicalStorySchema(many=True)

personal_background_schema = PersonalBackgroundSchema()
family_background_schema = FamilyBackgroundSchema()
profession_schema = ProfessionHistorySchema()
allergy_schema = AllergySchema()
vaccine_schema = VaccineSchema()
direction_schema = DirectionSchema()
municipality_schema = MunicipalitySchema()
state_schema = StateSchema()
country_schema = CountrySchema()


personal_background_schema_list = PersonalBackgroundSchema(many=True)
family_background_schema_list = FamilyBackgroundSchema(many=True)
profession_schema_list = ProfessionHistorySchema(many=True)
allergy_schema_list = AllergySchema(many=True)
vaccine_schema_list = VaccineSchema(many=True)

class Pacients(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        pacient_json = request.get_json()
        pacient = pacient_schema.load(pacient_json)

        if PacientModel.find_by_document(pacient.document):
            raise ResourceAlreadyExists("error", { "document": ["Ya existe un recurso con este campo"]})

        pacient.save_to_db()

        return {"success": True, "data": pacient_schema.dump(pacient)}, 201

    @classmethod
    @jwt_required
    def get(cls):
        query_params = request.args
        print(query_params)
        pacients = PacientModel.get_list(query_params)

        return { "success": True, "data": pacient_list_schema.dump(pacients) }, 200

class Pacient(Resource):
    @classmethod
    @jwt_required
    def get(cls, pacient_id: int):
        pacient = PacientModel.find_by_id(pacient_id)
        if not pacient:
            raise ResourceNotFound
        
        pacient = pacient_schema.dump(pacient)

        clinical_stories = ClinicalStoryModel.find_by_pacient_id(pacient_id)
        pacient["clinical_stories"] = clinical_story_schema_list.dump(clinical_stories)

        family_backgrounds = FamilyBackgroundModel.find_by_pacient_id(pacient_id)
        pacient["family_backgrounds"] = family_background_schema_list.dump(family_backgrounds)

        personal_backgrounds = PersonalBackgroundModel.find_by_pacient_id(pacient_id)
        pacient["personal_backgrounds"] = personal_background_schema_list.dump(personal_backgrounds)

        # allergies = AllergyModel.find_by_pacient_id(pacient_id)
        # pacient["allergies"] = allergy_schema_list.dump(allergies)

        vaccines = VaccineModel.find_by_pacient_id(pacient_id)
        pacient["vaccines"] = vaccine_schema_list.dump(vaccines)

        professions = ProfessionHistoryModel.find_by_pacient_id(pacient_id)
        pacient["professions"] = profession_schema_list.dump(professions)

        direction = DirectionModel.find_by_id(pacient["current_direction"])
        direction = direction_schema.dump(direction)

        municipality = MunicipalityModel.find_by_id(direction["municipality_id"])
        municipality = municipality_schema.dump(municipality)
        
        state = StateModel.find_by_id(municipality["state_id"])
        state = state_schema.dump(state)

        country = CountryModel.find_by_id(state["country_id"])
        country = country_schema.dump(country)

        direction["municipality"] = municipality
        direction["state"] = state
        direction["country"] = country

        pacient["direction"] = direction

        return { "success": True, "data": pacient }, 200

    @classmethod
    @jwt_required
    def put(cls, pacient_id: int):
        pacient = PacientModel.find_by_id(pacient_id)
        if not pacient:
            raise ResourceNotFound

        fields_json = request.get_json()
        supported_fields = ['gender', 'birth_date', 'current_direction', 'birth_direction', 'telephone1', 'telephone2', 'blood_type', 'marital_status']
        update_fields = { k : v for k, v in fields_json.items() if k in supported_fields}
        pacient.update(update_fields)
        return { "success": True, "data": pacient_schema.dump(pacient) }, 200
        
class PacientRelatedData(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        all_json = request.get_json()

        pacient_id = all_json["pacient_id"]
        
        if all_json["personal_background"]:
            for i, pb_id in enumerate(all_json["personal_background"]):
                personal_background_dict = {
                    "personal_background_type_id": pb_id,
                    "pacient_id": pacient_id
                }
                personal_background = personal_background_schema.load(personal_background_dict)
                personal_background.save_to_db()

        if all_json["family_background"]:
            fm_list = all_json.get("family_member")
            for i, fb_id in enumerate(all_json["family_background"]):
                family_background_dict = {
                    "family_background_type_id": fb_id,
                    "pacient_id": pacient_id,
                    "family_member": fm_list[i]
                }
                family_background = family_background_schema.load(family_background_dict)
                family_background.save_to_db()

        if all_json["profession"]:
            start_list = all_json.get("start")
            end_list = all_json.get("end")
            for i, p_id in enumerate(all_json["profession"]):
                profession_dict = {
                    "profession_type_id": p_id,
                    "pacient_id": pacient_id,
                    "start": start_list[i],
                    "end": end_list[i]
                }
                profession = profession_schema.load(profession_dict)
                profession.save_to_db()

        if all_json["vaccine"]:
            for i, v_id in enumerate(all_json["vaccine"]):
                vaccine_dict = {
                    "vaccine_type_id": v_id,
                    "pacient_id": pacient_id
                }
                vaccine = vaccine_schema.load(vaccine_dict)
                vaccine.save_to_db()

        return {"success": True, "data": { "pacient_id": all_json["pacient_id"]}}

class PacientImageUpload(Resource):
    @classmethod
    def post(cls, pacient_id):
        str_time = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]
        f = request.files['image']
        file_name = str_time + secure_filename(f.filename)
        f.save(file_name)


        pacient = PacientModel.find_by_id(pacient_id)

        pacient.img_url = file_name

        pacient.save_to_db()
        
        return { "success": True, "data": file_name }, 200