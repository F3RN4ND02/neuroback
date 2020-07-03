from resources.direction.direction import Directions, Direction

def init_direction_routes(api):
    api.add_resource(Directions, "/directions")
    api.add_resource(Direction, "/directions/<int:direction_id>")