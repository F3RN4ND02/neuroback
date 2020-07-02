from resources.allergy_type import Allergy

def init_allergies_routes(api):
    api.add_resource(Allergy, "/allergy_types")