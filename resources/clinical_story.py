from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import fresh_jwt_required, get_jwt_identity, jwt_required

from models.clinical_story import ClinicalStoryModel
from schemas.clinical_story import ClinicalStorySchema

from models.pacient import PacientModel

from utils.custom_errors import NotAuthorized, ResourceNotFound
from utils.try_decorator import try_except

clinical_story_schema = ClinicalStorySchema()


class CreateClinicalStory(Resource):
    @classmethod
    @fresh_jwt_required
    @try_except
    def post(cls):
        clinical_story_json = request.get_json()
        clinical_story_json['doctor_id'] = get_jwt_identity()

        pacient = PacientModel.find_by_id(clinical_story_json['pacient_id'])
        if not pacient:
            raise ResourceNotFound
        
        if pacient.doctor_id != get_jwt_identity():
            raise NotAuthorized
        
        clinical_story = clinical_story_schema.load(clinical_story_json)

        clinical_story.save_to_db()

        return {"success": True, "data": clinical_story_schema.dump(clinical_story)}, 201

class ClinicalStory(Resource):
    @classmethod
    @jwt_required
    @try_except
    def get(cls, clinical_story_id: int):
        clinical_story = ClinicalStoryModel.find_by_id(clinical_story_id)
        if not clinical_story:
            raise ResourceNotFound

        return { "success": True, "data": clinical_story_schema.dump(clinical_story) }, 200

    @classmethod
    @fresh_jwt_required
    @try_except
    def delete(cls, clinical_story_id: int):
        clinical_story = ClinicalStoryModel.find_by_id(clinical_story_id)
        if not clinical_story:
            raise ResourceNotFound

        if clinical_story.doctor_id != get_jwt_identity():
            raise NotAuthorized
        
        clinical_story.delete_from_db()
        return { "success": True, "data": {} }, 200

    @classmethod
    @fresh_jwt_required
    @try_except
    def put(cls, clinical_story_id: int):
        clinical_story = ClinicalStoryModel.find_by_id(clinical_story_id)
        if not clinical_story:
            raise ResourceNotFound

        if clinical_story.doctor_id != get_jwt_identity():
            raise NotAuthorized

        fields_json = request.get_json()
        supported_fields = ['title', 'description']
        update_fields = { k : v for k, v in fields_json.items() if k in supported_fields}
        clinical_story.update(update_fields)
        return { "success": True, "data": clinical_story_schema.dump(clinical_story) }, 200