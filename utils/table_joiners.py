
from models.clinical_story.medicine_type import MedicineTypeModel
from schemas.clinical_story.medicine_type import MedicineTypeSchema
medicine_type_schema = MedicineTypeSchema(many=True)

from models.clinical_story.symptom_type import SymptomTypeModel
from schemas.clinical_story.symptom_type import SymptomTypeSchema
symptom_type_schema = SymptomTypeSchema(many=True)

from models.clinical_story.metadata_type import MetadataTypeModel
from schemas.clinical_story.metadata_type import MetadataTypeSchema
metadata_type_schema = MetadataTypeSchema(many=True)

from models.pacient.backgrounds import BackgroundModel
from schemas.pacient.backgrounds import BackgroundSchema
backgrounds_schema = BackgroundSchema(many=True)

from models.pacient.profession_history import ProfessionHistoryModel
from schemas.pacient.profession_history import ProfessionHistorySchema
profession_schema_list = ProfessionHistorySchema(many=True)

# from models.pacient.allergy import AllergyTypeModel
# from schemas.pacient.allergy import AllergyTypeSchema
# allergy_type_schema_list = AllergySchema(many=True)

from models.pacient.vaccine_type import VaccineTypeModel
from schemas.pacient.vaccine_type import VaccineTypeSchema
vaccine_type_schema_list = VaccineTypeSchema(many=True)

from models.direction.direction import DirectionModel
from schemas.direction.direction import DirectionSchema
direction_schema_list = DirectionSchema(many=True)

from models.direction.direction import MunicipalityModel
from schemas.direction.municipality import MunicipalitySchema
municipality_schema_list = MunicipalitySchema(many=True)

from models.direction.direction import StateModel
from schemas.direction.state import StateSchema
state_schema_list = StateSchema(many=True)

from models.direction.direction import CountryModel
from schemas.direction.country import CountrySchema
country_schema_list = CountrySchema(many=True)


def get_types_data(tables):

    results = {}
    if "medicine_types" in tables:
        medicine_types = MedicineTypeModel.get_all()        
        results["medicine_types"] = medicine_type_schema.dump(medicine_types)

    if "symptom_types" in tables:
        symptom_types = SymptomTypeModel.get_all()        
        results["symptom_types"] = symptom_type_schema.dump(symptom_types)

    if "metadata_types" in tables:
        metadata_types = MetadataTypeModel.get_all()        
        results["metadata_types"] = metadata_type_schema.dump(metadata_types)

    if "backgrounds" in tables:
        background_types = BackgroundModel.get_all()        
        results["backgrounds"] = backgrounds_schema.dump(background_types)

    if "professional_history" in tables:
        professional_history = ProfessionalHistoryModel.get_all()        
        results["professional_history"] = professional_schema.dump(professional_history)

    if "vaccine_types" in tables:
        vaccine_types = VaccineTypeModel.get_all()        
        results["vaccine_types"] = vaccine_type_schema_list.dump(vaccine_types)

    if "directions" in tables:
        directions = DirectionModel.get_all()        
        results["directions"] = direction_schema_list.dump(directions)

    if "municipalities" in tables:
        municipalities = MunicipalityModel.get_all()        
        results["municipalities"] = state_schema_list.dump(municipalities)

    if "state" in tables:
        states = StateModel.get_all()        
        results["states"] = state_schema_list.dump(states)

    if "country" in tables:
        countries = CountryModel.get_all()        
        results["countries"] = country_schema_list.dump(countries)

    return results