from ma import ma
from models.pacient.vaccine import VaccineModel


class VaccineSchema(ma.ModelSchema):
    class Meta:
        model = VaccineModel
        dump_only = ("id",)
        include_fk = True