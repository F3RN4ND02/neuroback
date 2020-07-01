from flask_restful import Resource, request
from flask import request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import fresh_jwt_required, get_jwt_identity, jwt_required

from models.clinical_story.clinical_story import ClinicalStoryModel
from schemas.clinical_story.clinical_story import ClinicalStorySchema

from models.pacient.pacient import PacientModel

from models.clinical_story.medicine import MedicineModel
from schemas.clinical_story.medicine import MedicineSchema

from models.clinical_story.symptom import SymptomModel
from schemas.clinical_story.symptom import SymptomSchema

from models.clinical_story.exam_result import ExamResultModel
from schemas.clinical_story.exam_result import ExamResultSchema

from models.clinical_story.metadata import MetadataModel
from schemas.clinical_story.metadata import MetadataSchema

from utils.custom_errors import NotAuthorized, ResourceNotFound

clinical_story_schema = ClinicalStorySchema()
medicine_schema = MedicineSchema()
symptom_schema = SymptomSchema()
exam_schema = ExamResultSchema()
metadata_schema = MetadataSchema()

clinical_story_schema_list = ClinicalStorySchema(many=True)
medicine_schema_list = MedicineSchema(many=True)
symptom_schema_list = SymptomSchema(many=True)
exam_schema_list = ExamResultSchema(many=True)
metadata_schema_list = MetadataSchema(many=True)


class ClinicalStories(Resource):
    @classmethod
    @fresh_jwt_required
    def post(cls):
        clinical_story_json = request.get_json()
        clinical_story_json['user_id'] = get_jwt_identity()

        pacient = PacientModel.find_by_id(clinical_story_json['pacient_id'])
        if not pacient:
            raise ResourceNotFound
        
        clinical_story = clinical_story_schema.load(clinical_story_json)

        clinical_story.save_to_db()

        return {"success": True, "data": clinical_story_schema.dump(clinical_story)}, 201

    @classmethod
    @fresh_jwt_required
    def get(cls):
        query_params = request.args
        
        clinical_stories = ClinicalStoryModel.get_list(query_params)

        return {"success": True, "data": clinical_story_schema_list.dump(clinical_stories)}, 201

class ClinicalStory(Resource):
    @classmethod
    @jwt_required
    def get(cls, clinical_story_id: int):
        clinical_story = ClinicalStoryModel.find_by_id(clinical_story_id)
        if not clinical_story:
            raise ResourceNotFound

        return { "success": True, "data": clinical_story_schema.dump(clinical_story) }, 200

    @classmethod
    @fresh_jwt_required
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

class ClinicalStoryRelatedData(Resource):
    @classmethod
    @fresh_jwt_required
    def post(cls):
        all_json = request.get_json()

        if "medicine_id" in all_json:
            medicine_dict = {
                "medicine_type_id": all_json.get("medicine_id"),
                "clinical_story_id": all_json.get("clinical_story_id"),
                "background": all_json.get("background")
            }
            medicine = medicine_schema.load(medicine_dict)
            print(medicine)
            medicine.save_to_db()
        if "symptom_id" in all_json:
            symptom_dict = {
                "symptom_type_id": all_json.get("symptom_id"),
                "clinical_story_id": all_json.get("clinical_story_id")
            }
            symptom = symptom_schema.load(symptom_dict)
            print(symptom)
            symptom.save_to_db()

        if "exam_id" in all_json:
            exam_dict = {
                "exam_type_id": all_json.get("exam_id"),
                "clinical_story_id": all_json.get("clinical_story_id"),
                "result": all_json.get("result"),
                "date": all_json.get("date")
            }
            exam = exam_schema.load(exam_dict)
            exam.save_to_db()

        if "metadata_id" in all_json:
            metadata_dict = {
                "metadata_type_id": all_json.get("metadata_id"),
                "clinical_story_id": all_json.get("clinical_story_id"),
                "relevant": all_json.get("relevant")
            }
            metadata = metadata_schema.load(metadata_dict)
            metadata.save_to_db()

        return { "success": True, "data": { "clinical_story_id": all_json["clinical_story_id"]}}
