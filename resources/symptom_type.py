from flask_restful import Resource
from flask import request
from utils.metadata import pure_symptoms

from models.clinical_story.symptom_type import SymptomTypeModel
from schemas.clinical_story.symptom_type import SymptomTypeSchema

symptom_type_schema_list = SymptomTypeSchema(many=True)
symptom_type_schema = SymptomTypeSchema()

class CreateSymptoms(Resource):
    @classmethod
    def post(cls):
    
        name_list = []
        for metadata in pure_symptoms:
            for value in pure_symptoms[metadata]:
                if value not in name_list:
                    symptom_obj = {
                        "name": value,
                        "description": metadata
                    }
                    name_list.append(value)
        
                    symptom_obj = symptom_type_schema.load(symptom_obj)
                    symptom_obj.save_to_db()

        return { "success": True, "data": symptom_type_schema.dump(symptom_obj) }