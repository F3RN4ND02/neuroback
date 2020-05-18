from ma import ma
from models.direction.country import CountryModel


class CountrySchema(ma.ModelSchema):
    class Meta:
        model = CountryModel
        dump_only = ("id",)
