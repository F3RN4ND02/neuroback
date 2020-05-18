from ma import ma
from marshmallow import validates, ValidationError
from models.pacient.pacient import PacientModel

import datetime


class PacientSchema(ma.ModelSchema):
    class Meta:
        model = PacientModel
        dump_only = ("id","created_at","updated_at",)
        include_fk = True

    @validates('birth_date')
    def validate_birth_date(self, value):
        current_date = datetime.date.today()
        days = (current_date - value).days
        if days < 0:
            raise ValidationError("Invalid birth_date")
