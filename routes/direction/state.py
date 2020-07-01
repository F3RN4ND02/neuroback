from resources.direction.state import States

def init_state_routes(api):
    api.add_resource(States, "/states/<int:country_id>")