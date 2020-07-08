from flask_restful import Resource
from flask import request
   
from models.direction.direction import CountryModel
from schemas.direction.country import CountrySchema

from models.direction.direction import StateModel
from schemas.direction.state import StateSchema

from models.direction.direction import MunicipalityModel
from schemas.direction.municipality import MunicipalitySchema

from models.pacient.backgrounds import BackgroundModel
from schemas.pacient.backgrounds import BackgroundSchema

from models.pacient.allergy_type import AllergyTypeModel
from schemas.pacient.allergy_type import AllergyTypeSchema

from models.pacient.vaccine_type import VaccineTypeModel
from schemas.pacient.vaccine_type import VaccineTypeSchema

from models.clinical_story.medicine_type import MedicineTypeModel
from schemas.clinical_story.medicine_type import MedicineTypeSchema

from models.clinical_story.symptom_type import SymptomTypeModel
from schemas.clinical_story.symptom_type import SymptomTypeSchema

from models.clinical_story.metadata_type import MetadataTypeModel
from schemas.clinical_story.metadata_type import MetadataTypeSchema

country_schema = CountrySchema(many=True)
state_schema = StateSchema(many=True)
municipality_schema = MunicipalitySchema(many=True)
background_schema = BackgroundSchema(many=True)
vaccine_type_schema = VaccineTypeSchema(many=True)
medicine_type_schema = MedicineTypeSchema(many=True)
symptom_type_schema = SymptomTypeSchema(many=True) 
metadata_type_schema = MetadataTypeSchema(many=True) 

class ClinicalStoryFormData(Resource):
    @classmethod
    def get(cls):
        countries = CountryModel.query.all()
        states = StateModel.query.all()
        municipalities = MunicipalityModel.query.all()
        backgrounds = BackgroundModel.query.all()
        vaccines = VaccineTypeModel.query.all()
        medicines = MedicineTypeModel.query.all()
        symptoms = SymptomTypeModel.query.all()
        metadata = MetadataTypeModel.query.all()
        return {
            "success": True,
            "data": {
                "countries": country_schema.dump(countries),
                "states": state_schema.dump(states),
                "municipalities": municipality_schema.dump(municipalities),
                "backgrounds": background_schema.dump(backgrounds),
                "vaccines": vaccine_type_schema.dump(vaccines),
                "medicines": medicine_type_schema.dump(medicines),
                "symptoms": symptom_type_schema.dump(symptoms),
                "metadata": metadata_type_schema.dump(metadata)
            }
            }, 200


