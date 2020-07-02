from flask_restful import Resource
from flask import request
   
from models.pacient.backgrounds import BackgroundModel
from schemas.pacient.backgrounds import BackgroundSchema

background_schema_list = BackgroundSchema(many=True)
background_schema = BackgroundSchema()

class Background(Resource):
    @classmethod
    def post(cls):
        background_json = request.get_json()
        print(background_json)
        background = background_schema.load(background_json)

        background.save_to_db()

        return {"success": True, "data": background_schema.dump(background)}, 201

    @classmethod
    def get(cls):
        exams = BackgroundModel.get_list()

        return { "success": True, "data": background_schema_list.dump(exams) }, 200