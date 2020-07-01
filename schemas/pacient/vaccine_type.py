from ma import ma
from models.pacient.vaccine_type import VaccineTypeModel


class VaccineTypeSchema(ma.ModelSchema):
    class Meta:
        model = VaccineTypeModel
        dump_only = ("id",)