from resources.pacient import Pacients, Pacient, PacientRelatedData, PacientImageUpload

def init_pacient_routes(api):
    api.add_resource(Pacients, "/pacients")
    api.add_resource(Pacient, "/pacients/<int:pacient_id>")
    api.add_resource(PacientRelatedData, "/pacients/related_data")
    api.add_resource(PacientImageUpload, "/pacients/<int:pacient_id>/image")