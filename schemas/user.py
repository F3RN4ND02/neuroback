from ma import ma
from marshmallow import validates, validates_schema, ValidationError, fields
from models.user import UserModel

import datetime

fields.Field.default_error_messages["required"] = "Campo requerido"
fields.Field.default_error_messages["null"] = "El campo no puede estar vacio"
fields.Field.default_error_messages["validatior_failed"] = "Valor invalido"

class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id","created_at","updated_at","active",)

    confirm_password = fields.Str(required=True)

    @validates("password")
    def validate_password(self, value):
        if len(value) < 8 or len(value) > 16:
            raise ValidationError("La contraseña debe poseer entre 8 y 16 caracteres")


    # @validates("birth_date")
    # def validate_birth_date(self, value):
    #     current_date = datetime.date.today()
    #     age = (current_date - value).days / 365.25
    #     if age < 18:
    #         raise ValidationError("El usuario debe ser mayor de 18 años")

    @validates_schema
    def validate_password_confirmation(self, data, **kwargs):
        if data['password'] != data['confirm_password']:
            raise ValidationError("No coinciden las contraseñas")

