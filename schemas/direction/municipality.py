from ma import ma
from models.direction.direction import MunicipalityModel


class MunicipalitySchema(ma.ModelSchema):
    class Meta:
        model = MunicipalityModel
        dump_only = ("id",)
        include_fk = True