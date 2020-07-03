from flask_restful import Resource
from flask import request
   
from models.direction.direction import DirectionModel
from schemas.direction.direction import DirectionSchema

from models.direction.direction import CountryModel
from models.direction.direction import StateModel
from models.direction.direction import MunicipalityModel

from schemas.direction.country import CountrySchema
from schemas.direction.state import StateSchema
from schemas.direction.municipality import MunicipalitySchema

direction_schema = DirectionSchema()
municipality_schema = MunicipalitySchema()
state_schema = StateSchema()
country_schema = CountrySchema()


class Directions(Resource):
    @classmethod
    def post(cls):
        direction_json = request.get_json()
        direction = direction_schema.load(direction_json)

        direction.save_to_db()

        return {"success": True, "data": direction_schema.dump(direction)}, 201

class Direction(Resource):
    @classmethod
    def get(cls, direction_id):
        direction = DirectionModel.find_by_id(id=direction_id)

        if not direction:
            return {"success": False, "error": "Dirección no encontrada"}, 404

        direction = direction_schema.dump(direction)

        municipality = MunicipalityModel.find_by_id(direction["municipality_id"])
        municipality = municipality_schema.dump(municipality)
        
        state = StateModel.find_by_id(municipality["state_id"])
        state = state_schema.dump(state)

        country = CountryModel.find_by_id(state["country_id"])
        country = country_schema.dump(country)

        direction["municipality"] = municipality
        direction["state"] = state
        direction["country"] = country

        return {"success": True, "data": direction }, 201
        
