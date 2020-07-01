from resources.forms import ClinicalStoryFormData

def init_forms_routes(api):
    api.add_resource(ClinicalStoryFormData, "/form_data")
