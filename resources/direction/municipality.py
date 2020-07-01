from flask_restful import Resource
from flask import request
   
from models.direction.direction import MunicipalityModel
from schemas.direction.municipality import MunicipalitySchema


municipality_schema = MunicipalitySchema(many=True)

class Municipalities(Resource):
    @classmethod
    def get(cls, state_id: int):
        municipalities = MunicipalityModel.query.filter_by(state_id=state_id).all()
        return {"success": True, "data": municipality_schema.dump(municipalities)}, 200