from flask_restful import Resource
from flask import request
   
from models.direction.direction import CountryModel
from schemas.direction.country import CountrySchema


country_schema = CountrySchema(many=True)

class Countries(Resource):
    @classmethod
    def get(cls):
        countries = CountryModel.query.all()
        return {"success": True, "data": country_schema.dump(countries)}, 200