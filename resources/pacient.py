from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import jwt_required, fresh_jwt_required, get_jwt_identity
   
from models.pacient import PacientModel
from schemas.pacient import PacientSchema

from utils.custom_errors import NotAuthorized, ResourceNotFound
from utils.try_decorator import try_except

pacient_schema = PacientSchema()

class CreatePacient(Resource):
    @classmethod
    @fresh_jwt_required
    @try_except
    def post(cls):
        pacient_json = request.get_json()
        pacient_json['doctor_id'] = get_jwt_identity()
        pacient = pacient_schema.load(pacient_json)

        pacient.save_to_db()

        return {"success": True, "data": pacient_schema.dump(pacient)}, 201

class Pacient(Resource):
    @classmethod
    @jwt_required
    @try_except
    def get(cls, pacient_id: int):
        pacient = PacientModel.find_by_id(pacient_id)
        if not pacient:
            raise ResourceNotFound
        
        if pacient.doctor_id != get_jwt_identity():
            raise NotAuthorized

        return { "success": True, "data": pacient_schema.dump(pacient) }, 200

    @classmethod
    @fresh_jwt_required
    @try_except
    def delete(cls, pacient_id: int):
        pacient = PacientModel.find_by_id(pacient_id)
        if not pacient:
            raise ResourceNotFound

        if pacient.doctor_id != get_jwt_identity():
            raise NotAuthorized

        pacient.delete_from_db()
        return { "success": True, "data": {} }, 200

    @classmethod
    @fresh_jwt_required
    @try_except
    def put(cls, pacient_id: int):
        pacient = PacientModel.find_by_id(pacient_id)
        if not pacient:
            raise ResourceNotFound

        if pacient.doctor_id != get_jwt_identity():
            raise NotAuthorized

        fields_json = request.get_json()
        supported_fields = ['gender', 'birth_date', 'living_city']
        update_fields = { k : v for k, v in fields_json.items() if k in supported_fields}
        pacient.update(update_fields)
        return { "success": True, "data": pacient_schema.dump(pacient) }, 200