from resources.direction.municipality import Municipalities

def init_municipality_routes(api):
    api.add_resource(Municipalities, "/municipalities/<int:state_id>")