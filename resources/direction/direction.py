from flask_restful import Resource
from flask import request
   
from models.direction.direction import DirectionModel
from schemas.direction.direction import DirectionSchema

from models.direction.direction import CountryModel
from models.direction.direction import StateModel
from models.direction.direction import MunicipalityModel

direction_schema = DirectionSchema()

class Direction(Resource):
    @classmethod
    def post(cls):
        direction_json = request.get_json()
        print(direction_json)
        direction = direction_schema.load(direction_json)

        direction.save_to_db()

        return {"success": True, "data": direction_schema.dump(direction)}, 201