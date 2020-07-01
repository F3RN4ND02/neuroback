from flask_restful import Resource
from flask import request
   
from models.direction.direction import StateModel
from schemas.direction.state import StateSchema


state_schema = StateSchema(many=True)

class States(Resource):
    @classmethod
    def get(cls, country_id: int):
        states = StateModel.query.filter_by(country_id=country_id).all()
        return {"success": True, "data": state_schema.dump(states)}, 200