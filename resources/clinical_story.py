from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import fresh_jwt_required, get_jwt_identity, jwt_required

from models.clinical_story import ClinicalStoryModel
from schemas.clinical_story import ClinicalStorySchema

from models.pacient import PacientModel

clinical_story_schema = ClinicalStorySchema()

BLANK_ERROR = "'{}' cannot be blank."
STORY_NOT_FOUND = "Story not found."
STORY_DELETED = "Story deleted."
NO_ACCESS = "You have not access to this story"

class CreateClinicalStory(Resource):
    @classmethod
    @fresh_jwt_required
    def post(cls):
        clinical_story_json = request.get_json()
        clinical_story_json['doctor_id'] = get_jwt_identity()

        pacient = PacientModel.find_by_id(clinical_story_json['pacient_id'])
        if not pacient:
            return {"success": False, "error": "Pacient not found"}, 404
        
        if pacient.doctor_id != get_jwt_identity():
            return {"success": False, "error": "You cannot access this pacient"}, 404
        
        clinical_story = clinical_story_schema.load(clinical_story_json)

        clinical_story.save_to_db()

        return {"success": True, "data": clinical_story_schema.dump(clinical_story)}, 201

class ClinicalStory(Resource):
    @classmethod
    @jwt_required
    def get(cls, clinical_story_id: int):
        clinical_story = ClinicalStoryModel.find_by_id(clinical_story_id)
        if not clinical_story:
            return {"success": False, "error": STORY_NOT_FOUND}, 404

        return { "success": True, "data": clinical_story_schema.dump(clinical_story) }, 200

    @classmethod
    @fresh_jwt_required
    def delete(cls, clinical_story_id: int):
        clinical_story = ClinicalStoryModel.find_by_id(clinical_story_id)
        if not clinical_story:
            return {"success": False, "error": STORY_NOT_FOUND}, 404

        if clinical_story.doctor_id != get_jwt_identity():
            return {"success": False, "error": NO_ACCESS}, 401
        
        clinical_story.delete_from_db()
        return { "success": True, "data": {} }, 200

    @classmethod
    @fresh_jwt_required
    def put(cls, clinical_story_id: int):
        clinical_story = ClinicalStoryModel.find_by_id(clinical_story_id)
        if not clinical_story:
            return {"success": False, "error": STORY_NOT_FOUND}, 404

        if clinical_story.doctor_id != get_jwt_identity():
            return {"success": False, "error": NO_ACCESS}, 401

        fields_json = request.get_json()
        supported_fields = ['title', 'description']
        update_fields = { k : v for k, v in fields_json.items() if k in supported_fields}
        clinical_story.update(update_fields)
        return { "success": True, "data": clinical_story_schema.dump(clinical_story) }, 200