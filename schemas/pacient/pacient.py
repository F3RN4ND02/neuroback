from ma import ma
from marshmallow import validates, ValidationError, pre_load
from models.pacient.pacient import PacientModel

import datetime


class PacientSchema(ma.ModelSchema):
    class Meta:
        model = PacientModel
        dump_only = ("id","created_at","updated_at",)
        include_fk = True

    @pre_load
    def correct_enum(self, data, **kwargs):
        if "gender" in data:
            data["gender"] = data["gender"].lower()
        
        if "marital_status" in data:
            data["marital_status"] = data["marital_status"].lower()

        return data

    @validates('birth_date')
    def validate_birth_date(self, value):
        current_date = datetime.date.today()
        days = (current_date - value).days
        if days < 0:
            raise ValidationError("Invalid birth_date")
