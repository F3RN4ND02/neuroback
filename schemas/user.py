from ma import ma
from marshmallow import validates, ValidationError
from models.user import UserModel

import datetime


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id","created_at","updated_at","active",)

    @validates("password")
    def validate_password(self, value):
        if len(value) < 8 or len(value) > 16:
            raise ValidationError("Password length must be between 8 and 16 characters")

    @validates("birth_date")
    def validate_birth_date(self, value):
        current_date = datetime.date.today()
        age = (current_date - value).days / 365.25
        if age < 18:
            raise ValidationError("User must be at least 18 years old")

