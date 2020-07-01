from flask_restful import Resource
from flask import request
   
from models.direction.direction import CountryModel
from schemas.direction.country import CountrySchema

from models.pacient.backgrounds import BackgroundModel
from schemas.pacient.backgrounds import BackgroundSchema

from models.pacient.allergy_type import AllergyTypeModel
from schemas.pacient.allergy_type import AllergyTypeSchema

from models.pacient.vaccine_type import VaccineTypeModel
from schemas.pacient.vaccine_type import VaccineTypeSchema

from models.clinical_story.medicine_type import MedicineTypeModel
from schemas.clinical_story.medicine_type import MedicineTypeSchema

country_schema = CountrySchema(many=True)
background_schema = BackgroundSchema(many=True)
allergy_type_schema = AllergyTypeSchema(many=True)
vaccine_type_schema = VaccineTypeSchema(many=True)
medicine_type_schema = MedicineTypeSchema(many=True) 

class ClinicalStoryFormData(Resource):
    @classmethod
    def get(cls):
        countries = CountryModel.query.all()
        backgrounds = BackgroundModel.query.all()
        allergies = AllergyTypeModel.query.all()
        vaccines = VaccineTypeModel.query.all()
        medicines = MedicineTypeModel.query.all()
        return {
            "success": True,
            "data": {
                "countries": country_schema.dump(countries),
                "backgrounds": background_schema.dump(backgrounds),
                "allergies": allergy_type_schema.dump(allergies),
                "vaccines": vaccine_type_schema.dump(vaccines),
                "medicines": medicine_type_schema.dump(medicines),
            }
            }, 200