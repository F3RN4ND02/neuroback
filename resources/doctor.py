from flask_restful import Resource
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt,
)
from models.doctor import DoctorModel
from schemas.doctor import DoctorSchema
from blacklist import BLACKLIST
from utils.try_decorator import try_except
from utils.custom_errors import ResourceAlreadyExists, ResourceNotFound, InvalidCredentials, NotAuthorized

doctor_schema = DoctorSchema()

DOCTOR_DELETED = "Doctor deleted."
DOCTOR_LOGGED_OUT = "Doctor <id={}> successfully logged out."

class DoctorRegister(Resource):
    @classmethod
    @try_except
    def post(cls):
        doctor_json = request.get_json()
        doctor = doctor_schema.load(doctor_json)

        if DoctorModel.find_by_email(doctor.email):
            raise ResourceAlreadyExists

        doctor.password = generate_password_hash(doctor.password, method='sha256')
        doctor.save_to_db()

        return {"success": True, "data": doctor_schema.dump(doctor)}, 201

class DoctorLogin(Resource):
    @classmethod
    @try_except
    def post(cls):
        doctor_json = request.get_json()

        doctor = DoctorModel.find_by_email(doctor_json['email'])

        if doctor and check_password_hash(doctor.password, doctor_json['password']):
            access_token = create_access_token(identity=doctor.id, fresh=True)
            refresh_token = create_refresh_token(doctor.id)
            return {"success": True, "access_token": access_token, "refresh_token": refresh_token}, 200

        raise InvalidCredentials

class DoctorLogout(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        doctor_id = get_jwt_identity()
        BLACKLIST.add(jti)
        return {"success": True, "message": DOCTOR_LOGGED_OUT.format(doctor_id)}, 200

class Doctor(Resource):
    @classmethod
    @try_except
    def get(cls, doctor_id: int):
        doctor = DoctorModel.find_by_id(doctor_id)
        if not doctor:
            raise ResourceNotFound

        return { "success": True, "data": doctor_schema.dump(doctor) }, 200

    @classmethod
    @jwt_required
    @try_except
    def delete(cls, doctor_id: int):
        doctor = DoctorModel.find_by_id(doctor_id)
        if not doctor:
            raise ResourceNotFound

        if doctor_id != get_jwt_identity():
            raise NotAuthorized

        doctor.delete_from_db()
        return { "success": True, "data": {} }, 200

    @classmethod
    @jwt_required
    @try_except
    def put(cls, doctor_id: int):
        doctor = DoctorModel.find_by_id(doctor_id)
        if not doctor:
            raise ResourceNotFound

        if doctor_id != get_jwt_identity():
            raise NotAuthorized

        fields_json = request.get_json()
        supported_fields = ['first_name', 'last_name', 'birth_date', 'work_city']
        update_fields = { k : v for k, v in fields_json.items() if k in supported_fields}
        doctor.update(update_fields)
        return { "success": True, "data": doctor_schema.dump(doctor) }, 200