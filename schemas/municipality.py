from ma import ma
from models.municipality import MunicipalityModel


class MunicipalitySchema(ma.ModelSchema):
    class Meta:
        model = MunicipalityModel
        dump_only = ("id",)