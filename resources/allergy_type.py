from flask_restful import Resource
from flask import request
   
from models.pacient.allergy_type import AllergyTypeModel
from schemas.pacient.allergy_type import AllergyTypeSchema

allergy_schema_list = AllergyTypeSchema(many=True)
allergy_schema = AllergyTypeSchema()

class Allergy(Resource):
    @classmethod
    def post(cls):
        allergy_json = request.get_json()
        print(allergy_json)
        allergy = allergy_schema.load(allergy_json)

        allergy.save_to_db()

        return {"success": True, "data": allergy_schema.dump(allergy)}, 201

    @classmethod
    def get(cls):
        exams = AllergyTypeModel.get_list()

        return { "success": True, "data": allergy_schema_list.dump(exams) }, 200