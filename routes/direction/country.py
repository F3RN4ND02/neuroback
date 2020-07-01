from resources.direction.country import Countries

def init_country_routes(api):
    api.add_resource(Countries, "/countries")