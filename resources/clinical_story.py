from flask_restful import Resource, request
from flask import request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import fresh_jwt_required, get_jwt_identity, jwt_required
from tensorflow.keras.models import load_model
import numpy as np
from utils.metadata import metadata

nn_model = load_model("full.h5")

from models.clinical_story.clinical_story import ClinicalStoryModel
from schemas.clinical_story.clinical_story import ClinicalStorySchema

from models.pacient.pacient import PacientModel
from schemas.pacient.pacient import PacientSchema

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
pacient_schema = PacientSchema()

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
    @jwt_required
    def get(cls):
        query_params = request.args
        
        clinical_stories = ClinicalStoryModel.get_list(query_params)

        clinical_stories = clinical_story_schema_list.dump(clinical_stories)

        for clc_story in clinical_stories:
            c_id = clc_story["id"]
            medicines = MedicineModel.find_by_story_id(c_id)
            medicines = medicine_schema_list.dump(medicines)

            symptoms = SymptomModel.find_by_story_id(c_id)
            symptoms = symptom_schema_list.dump(symptoms)

            exams = ExamResultModel.find_by_story_id(c_id)
            exams = exam_schema_list.dump(exams)
            

            clc_story["medicines"] = medicines
            clc_story["symptoms"] = symptoms
            clc_story["exams"] = exams
            
        
        return {"success": True, "data": clinical_stories}, 201

class ClinicalStory(Resource):
    @classmethod
    @jwt_required
    def get(cls, clinical_story_id: int):
        clinical_story = ClinicalStoryModel.find_by_id(clinical_story_id)
        if not clinical_story:
            raise ResourceNotFound

        clinical_story = clinical_story_schema.dump(clinical_story)

        medicines = MedicineModel.find_by_story_id(clinical_story["id"])
        medicines = medicine_schema_list.dump(medicines)

        symptoms = SymptomModel.find_by_story_id(clinical_story["id"])
        symptoms = symptom_schema_list.dump(symptoms)

        exams = ExamResultModel.find_by_story_id(clinical_story["id"])
        exams = exam_schema_list.dump(exams)

        pacient = PacientModel.find_by_id(clinical_story["pacient_id"])
        pacient = pacient_schema.dump(pacient)

        clinical_story["medicines"] = medicines
        clinical_story["symptoms"] = symptoms
        clinical_story["exams"] = exams
        clinical_story["pacient"] = pacient

        return { "success": True, "data": clinical_story }, 200

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

        clinical_story_id = all_json.get("clinical_story_id")
        
        if "medicine_id" in all_json:
            b_list = all_json.get("background")
            for i, med_id in enumerate(all_json["medicine_id"]):
                medicine_dict = {
                    "medicine_type_id": med_id,
                    "clinical_story_id": clinical_story_id,
                    "background": b_list[i]
                }
                medicine = medicine_schema.load(medicine_dict)
                medicine.save_to_db()

        if "symptom_id" in all_json:
            for i, s_id in enumerate(all_json.get("symptom_id")):
                symptom_dict = {
                    "symptom_type_id": s_id,
                    "clinical_story_id": clinical_story_id
                }
                symptom = symptom_schema.load(symptom_dict)
                symptom.save_to_db()

        if "exam_id" in all_json:
            result_list = all_json.get("result")
            date_list = all_json.get("date")
            for i, ex_id in enumerate(all_json.get("exam_id")):
                exam_dict = {
                    "exam_type_id": ex_id,
                    "clinical_story_id": clinical_story_id,
                    "result": result_list[i],
                    "date": date_list[i]
                }
                exam = exam_schema.load(exam_dict)
                exam.save_to_db()

        if "metadata_id" in all_json:
            relevant_list = all_json.get("relevant")
            for i, m_id in enumerate(all_json.get("metadata_id")):
                metadata_dict = {
                    "metadata_type_id": m_id,
                    "clinical_story_id": clinical_story_id,
                    "relevant": relevant_list[i]
                }
                metadata = metadata_schema.load(metadata_dict)
                metadata.save_to_db()

        return { "success": True, "data": { "clinical_story_id": all_json["clinical_story_id"]}}

class GetHelp(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        NUMBER_OF_STORIES = 8

        metadata_json = request.get_json()

        input_data = np.array([metadata_json["metadata"]])

        prediction_result = nn_model.predict(input_data)

        present_metadata = []
        values = []
        relevant = {}
        for i, meta in enumerate(metadata_json["metadata"]):
            if meta == 1:
                # present_metadata.append(i)
                # values.append(prediction_result[0][i])
                relevant[i] = prediction_result[0][i]
        relevant = {k: v for k, v in sorted(relevant.items(), key=lambda item: item[1], reverse=True)}
        print(relevant)

        clinical_stories = []
        for key in relevant:
            metadata_results = MetadataModel.find_by_story_id(key + 1)
            metadata_results = metadata_schema_list.dump(metadata_results)

            for result in metadata_results:
                clinical_story = ClinicalStoryModel.find_by_id(result["clinical_story_id"])
                clinical_story = clinical_story_schema.dump(clinical_story)

                c_id = clinical_story["id"]

                medicines = MedicineModel.find_by_story_id(c_id)
                medicines = medicine_schema_list.dump(medicines)

                symptoms = SymptomModel.find_by_story_id(c_id)
                symptoms = symptom_schema_list.dump(symptoms)

                exams = ExamResultModel.find_by_story_id(c_id)
                exams = exam_schema_list.dump(exams)
                

                clinical_story["medicines"] = medicines
                clinical_story["symptoms"] = symptoms
                clinical_story["exams"] = exams

                clinical_stories.append(clinical_story)

        return {"success": True, "data": clinical_stories}, 200
        