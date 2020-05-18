from ma import ma
from models.direction.municipality import MunicipalityModel


class MunicipalitySchema(ma.ModelSchema):
    class Meta:
        model = MunicipalityModel
        dump_only = ("id",)