from resources.backgrounds import Background

def init_backgrounds_routes(api):
    api.add_resource(Background, "/backgrounds")