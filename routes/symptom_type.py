from resources.symptom_type import CreateSymptoms

def init_symptoms_routes(api):
    api.add_resource(CreateSymptoms, "/create_symptoms")