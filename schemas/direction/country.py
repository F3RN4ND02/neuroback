from ma import ma
from models.direction.direction import CountryModel


class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CountryModel
        dump_only = ("id",)
