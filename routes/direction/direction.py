from resources.direction.direction import Direction

def init_direction_routes(api):
    api.add_resource(Direction, "/directions")