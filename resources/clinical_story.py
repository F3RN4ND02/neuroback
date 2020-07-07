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
clinical_story_schema = ClinicalStorySchema()
clinical_story_schema_list = ClinicalStorySchema(many=True)

from models.pacient.pacient import PacientModel
from schemas.pacient.pacient import PacientSchema
pacient_schema = PacientSchema()
pacient_schema_list = PacientSchema(many=True)


from models.clinical_story.medicine import MedicineModel
from schemas.clinical_story.medicine import MedicineSchema
medicine_schema = MedicineSchema()
medicine_schema_list = MedicineSchema(many=True)
from models.clinical_story.medicine_type import MedicineTypeModel
from schemas.clinical_story.medicine_type import MedicineTypeSchema
medicine_type_schema = MedicineTypeSchema(many=True)


from models.clinical_story.symptom import SymptomModel
from schemas.clinical_story.symptom import SymptomSchema
symptom_schema = SymptomSchema()
symptom_schema_list = SymptomSchema(many=True)
from models.clinical_story.symptom_type import SymptomTypeModel
from schemas.clinical_story.symptom_type import SymptomTypeSchema
symptom_type_schema = SymptomTypeSchema(many=True)

from models.clinical_story.exam_result import ExamResultModel
from schemas.clinical_story.exam_result import ExamResultSchema
exam_schema = ExamResultSchema()
exam_schema_list = ExamResultSchema(many=True)
from models.clinical_story.exam_type import ExamTypeModel
from schemas.clinical_story.exam_type import ExamTypeSchema
exam_type_schema = ExamTypeSchema(many=True)

from models.clinical_story.metadata import MetadataModel
from schemas.clinical_story.metadata import MetadataSchema
metadata_schema = MetadataSchema()
metadata_schema_list = MetadataSchema(many=True)
from models.clinical_story.metadata_type import MetadataTypeModel
from schemas.clinical_story.metadata_type import MetadataTypeSchema
metadata_type_schema = MetadataTypeSchema(many=True)

from models.pacient.vaccine import VaccineModel
from schemas.pacient.vaccine import VaccineSchema 
vaccine_schema_list = VaccineSchema(many=True)

from models.pacient.personal_background import PersonalBackgroundModel
from schemas.pacient.personal_background import PersonalBackgroundSchema 
personal_background_schema_list = PersonalBackgroundSchema(many=True)

from models.pacient.family_background import FamilyBackgroundModel
from schemas.pacient.family_background import FamilyBackgroundSchema 
family_background_schema_list = FamilyBackgroundSchema(many=True)

from models.direction.direction import DirectionModel
from schemas.direction.direction import DirectionSchema 
direction_schema = DirectionSchema()

from models.direction.direction import MunicipalityModel
from schemas.direction.municipality import MunicipalitySchema 
municipality_schema = MunicipalitySchema()

from utils.custom_errors import NotAuthorized, ResourceNotFound
from utils.table_joiners import get_types_data

class ClinicalStories(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        clinical_story_json = request.get_json()
        clinical_story_json['user_id'] = get_jwt_identity()

        pacient = PacientModel.find_by_id(clinical_story_json['pacient_id'])
        if not pacient:
            raise ResourceNotFound
        
        related_data = None
        if "related_data" in clinical_story_json: 
            related_data = clinical_story_json.pop("related_data") 
        
        clinical_story = clinical_story_schema.load(clinical_story_json)

        clinical_story.save_to_db()

        medicines = list()
        symptoms = list()
        exams = list()
        metadata = list()

        if related_data:
            all_json = related_data
            print(all_json)
            if "medicine_id" in all_json:
                b_list = all_json.get("background")
                for i, med_id in enumerate(all_json["medicine_id"]):
                    medicine_dict = {
                        "medicine_type_id": med_id,
                        "clinical_story_id": clinical_story.id,
                        "background": b_list[i]
                    }
                    medicines.append(medicine_schema.load(medicine_dict))
                    print(medicines)
            if "symptom_id" in all_json:
                for i, s_id in enumerate(all_json.get("symptom_id")):
                    symptom_dict = {
                        "symptom_type_id": s_id,
                        "clinical_story_id": clinical_story.id
                    }
                    symptoms.append(symptom_schema.load(symptom_dict))
                    print(symptoms)

            if "exam_id" in all_json:
                result_list = all_json.get("result")
                date_list = all_json.get("date")
                for i, ex_id in enumerate(all_json.get("exam_id")):
                    exam_dict = {
                        "exam_type_id": ex_id,
                        "clinical_story_id": clinical_story.id,
                        "result": result_list[i],
                        "date": date_list[i]
                    }
                    exams.append(exam_schema.load(exam_dict))
                    print(exams)
            if "metadata_id" in all_json:
                relevant_list = all_json.get("relevant")
                for i, m_id in enumerate(all_json.get("metadata_id")):
                    metadata_dict = {
                        "metadata_type_id": m_id,
                        "clinical_story_id": clinical_story.id,
                        "relevant": relevant_list[i]
                    }
                    metadata.append(metadata_schema.load(metadata_dict))
                    
            if "medicine_id" in all_json: 
                for medicine in medicines:
                    print(medicine)
                    medicine.save_to_db()
            if "symptom_id" in all_json: 
                for symptom in symptoms:   
                    symptom.save_to_db()
            if "exam_id" in all_json:
                for exam in exams:
                    exam.save_to_db()
            if "metadata_id" in all_json: 
                for meta in metadata:
                    meta.save_to_db()

        


        return {"success": True, "data": clinical_story_schema.dump(clinical_story)}, 201

    @classmethod
    @jwt_required
    def get(cls):
        query_params = request.args
        
        clinical_stories = ClinicalStoryModel.get_list(query_params)

        clinical_stories = clinical_story_schema_list.dump(clinical_stories)

        types = get_types_data(["medicine_types", "symptom_types", "metadata_types", "backgrounds", "vaccine_types", "directions", "municipalities", "states", "countries"])

        for clc_story in clinical_stories:
            c_id = clc_story["id"]

            medicines = MedicineModel.find_by_story_id(c_id)
            medicines = medicine_schema_list.dump(medicines)
            med_ids = [med["medicine_type_id"] for med in medicines]
            clc_medicines = []
            for med in types["medicine_types"]:
                if med["id"] in med_ids:
                    clc_medicines.append({ "id": med["id"], "nombre": med["nombre"], "principio_activo": med["principio_activo"], "presentacion": med["presentacion"] })
            
            symptoms = SymptomModel.find_by_story_id(c_id)
            symptoms = symptom_schema_list.dump(symptoms)
            symp_ids = [symp["symptom_type_id"] for symp in symptoms]
            clc_symptoms = []
            for symp in types["symptom_types"]:
                if symp["id"] in symp_ids:
                    clc_symptoms.append({ "id": symp["id"], "name": symp["name"], "description": symp["description"] })
            
            metadata = MetadataModel.find_by_story_id(c_id)
            metadata = metadata_schema_list.dump(metadata)
            metadata_ids = [metadata["metadata_type_id"] for metadata in metadata]
            clc_metadata = []
            for metadata in types["metadata_types"]:
                if metadata["id"] in metadata_ids:
                    clc_metadata.append({ "id": metadata["id"], "name": metadata["name"], "description": metadata["description"] })

            
            
            pacient = PacientModel.find_by_id(clc_story["pacient_id"])
            pacient = pacient_schema.dump(pacient)
            p_id = pacient["id"]

            personal_backgrounds = PersonalBackgroundModel.find_by_pacient_id(p_id)
            personal_backgrounds = personal_background_schema_list.dump(personal_backgrounds)
            personal_background_ids = [personal_background["personal_background_type_id"] for personal_background in personal_backgrounds]
            p_personal_backgrounds = []
            for personal_background in types["backgrounds"]:
                if personal_background["id"] in personal_background_ids:
                    p_personal_backgrounds.append({ "id": personal_background["id"], "name": personal_background["name"], "description": personal_background["description"] })

            family_backgrounds = FamilyBackgroundModel.find_by_pacient_id(p_id)
            family_backgrounds = family_background_schema_list.dump(family_backgrounds)
            family_background_ids = [family_background["family_background_type_id"] for family_background in family_backgrounds]
            p_family_backgrounds = []
            for family_background in types["backgrounds"]:
                if family_background["id"] in family_background_ids:
                    p_family_backgrounds.append({ "id": family_background["id"], "name": family_background["name"], "description": family_background["description"] })

            vaccines = VaccineModel.find_by_pacient_id(p_id)
            vaccines = vaccine_schema_list.dump(vaccines)
            vaccine_ids = [vaccine["vaccine_type_id"] for vaccine in vaccines]
            p_vaccines = []
            for vaccine in types["vaccine_types"]:
                if vaccine["id"] in vaccine_ids:
                    p_vaccines.append({ "id": vaccine["id"], "name": vaccine["name"], "description": vaccine["description"] })

            direction = DirectionModel.find_by_id(pacient["current_direction"])
            direction = direction_schema.dump(direction)
            municipality = MunicipalityModel.find_by_id(direction["municipality_id"])
            municipality = municipality_schema.dump(municipality)
            direction["municipality"] = municipality

            pacient["personal_backgrounds"] = p_personal_backgrounds
            pacient["family_backgrounds"] = p_family_backgrounds
            pacient["vaccines"] = p_vaccines
            pacient["direction"] = direction

            clc_story["pacient"] = pacient
            clc_story["medicines"] = clc_medicines
            clc_story["symptoms"] = clc_symptoms
            clc_story["metadata"] = clc_metadata
            
        
        return {"success": True, "data": clinical_stories}, 201

class ClinicalStory(Resource):
    @classmethod
    @jwt_required
    def get(cls, clinical_story_id: int):
        clinical_story = ClinicalStoryModel.find_by_id(clinical_story_id)
        if not clinical_story:
            raise ResourceNotFound

        clinical_story = clinical_story_schema.dump(clinical_story)

        pacient = PacientModel.find_by_id(clinical_story["pacient_id"])
        pacient = pacient_schema.dump(pacient)

        types = get_types_data(["medicine_types", "symptom_types", "metadata_types", "backgrounds", "vaccine_types", "directions", "municipalities", "states", "countries"])

        c_id = clinical_story["id"]

        medicines = MedicineModel.find_by_story_id(c_id)
        medicines = medicine_schema_list.dump(medicines)
        med_ids = [med["medicine_type_id"] for med in medicines]
        clc_medicines = []
        for med in types["medicine_types"]:
            if med["id"] in med_ids:
                clc_medicines.append({ "id": med["id"], "nombre": med["nombre"], "principio_activo": med["principio_activo"], "presentacion": med["presentacion"] })
        
        symptoms = SymptomModel.find_by_story_id(c_id)
        symptoms = symptom_schema_list.dump(symptoms)
        symp_ids = [symp["symptom_type_id"] for symp in symptoms]
        clc_symptoms = []
        for symp in types["symptom_types"]:
            if symp["id"] in symp_ids:
                clc_symptoms.append({ "id": symp["id"], "name": symp["name"], "description": symp["description"] })
        
        metadata = MetadataModel.find_by_story_id(c_id)
        metadata = metadata_schema_list.dump(metadata)
        metadata_ids = [metadata["metadata_type_id"] for metadata in metadata]
        clc_metadata = []
        for metadata in types["metadata_types"]:
            if metadata["id"] in metadata_ids:
                clc_metadata.append({ "id": metadata["id"], "name": metadata["name"], "description": metadata["description"] })

        clinical_story["pacient"] = pacient
        clinical_story["medicines"] = clc_medicines
        clinical_story["symptoms"] = clc_symptoms
        clinical_story["metadata"] = clc_metadata
        return { "success": True, "data": clinical_story }, 200

    @classmethod
    @jwt_required
    def delete(cls, clinical_story_id: int):
        clinical_story = ClinicalStoryModel.find_by_id(clinical_story_id)
        if not clinical_story:
            raise ResourceNotFound


        if clinical_story.doctor_id != get_jwt_identity():
            raise NotAuthorized
        
        clinical_story.delete_from_db()
        return { "success": True, "data": {} }, 200

    @classmethod
    @jwt_required
    def put(cls, clinical_story_id: int):
        clinical_story = ClinicalStoryModel.find_by_id(clinical_story_id)
        if not clinical_story:
            raise ResourceNotFound

        if clinical_story.doctor_id != get_jwt_identity():
            raise NotAuthorized

        fields_json = request.get_json()
        supported_fields = ['diagnosis', 'description', 'fisical_exams', 'observations']
        update_fields = { k : v for k, v in fields_json.items() if k in supported_fields}
        clinical_story.update(update_fields)
        return { "success": True, "data": clinical_story_schema.dump(clinical_story) }, 200

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
        