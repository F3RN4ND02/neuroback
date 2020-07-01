from ma import ma
from models.direction.direction import MunicipalityModel


class MunicipalitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MunicipalityModel
        dump_only = ("id",)