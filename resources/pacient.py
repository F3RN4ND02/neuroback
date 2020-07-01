from flask_restful import Resource, request
from flask import request
from werkzeug.security import safe_str_cmp
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

from utils.custom_errors import ResourceAlreadyExists, NotAuthorized, ResourceNotFound

pacient_schema = PacientSchema()
pacient_list_schema = PacientSchema(many=True)

clinical_story_schema_list = ClinicalStorySchema(many=True)

personal_background_schema = PersonalBackgroundSchema()
family_background_schema = FamilyBackgroundSchema()
profession_schema = ProfessionHistorySchema()
allergy_schema = AllergySchema()
vaccine_schema = VaccineSchema()

personal_background_schema_list = PersonalBackgroundSchema(many=True)
family_background_schema_list = FamilyBackgroundSchema(many=True)
profession_schema_list = ProfessionHistorySchema(many=True)
allergy_schema_list = AllergySchema(many=True)
vaccine_schema_list = VaccineSchema(many=True)

class Pacients(Resource):
    @classmethod
    @fresh_jwt_required
    def post(cls):
        pacient_json = request.get_json()
        pacient = pacient_schema.load(pacient_json)

        if PacientModel.find_by_document(pacient.document):
            raise ResourceAlreadyExists("error", { "document": ["Ya existe un recurso con este campo"]})

        pacient.save_to_db()

        return {"success": True, "data": pacient_schema.dump(pacient)}, 201

    @classmethod
    @fresh_jwt_required
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

        return { "success": True, "data": pacient }, 200

    @classmethod
    @fresh_jwt_required
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

        if all_json["personal_background"]:
            personal_background_dict = {
                "personal_background_type_id": all_json["personal_background"],
                "pacient_id": all_json["pacient_id"]
            }
            personal_background = personal_background_schema.load(personal_background_dict)
            print(personal_background)
            personal_background.save_to_db()

        if all_json["family_background"]:
            family_background_dict = {
                "family_background_type_id": all_json["family_background"],
                "pacient_id": all_json["pacient_id"],
                "family_member": all_json.get("family_member")
            }
            family_background = family_background_schema.load(family_background_dict)
            family_background.save_to_db()

        if all_json["profession"]:
            profession_dict = {
                "profession_type_id": all_json["profession"],
                "pacient_id": all_json["pacient_id"],
                "start": all_json.get("start"),
                "end": all_json.get("end")
            }
            profession = profession_schema.load(profession_dict)
            profession.save_to_db()

        # if all_json["allergy"]:
        #     allergy_dict = {
        #         "allergy_type_id": all_json["allergy"],
        #         "pacient_id": all_json["pacient_id"]
        #     }
        #     allergy = allergy_schema.load(allergy_dict)
        #     allergy.save_to_db()

        if all_json["vaccine"]:
            vaccine_dict = {
                "vaccine_type_id": all_json["vaccine"],
                "pacient_id": all_json["pacient_id"]
            }
            vaccine = vaccine_schema.load(vaccine_dict)
            vaccine.save_to_db()

        return {"success": True, "data": { "pacient_id": all_json["pacient_id"]}}
