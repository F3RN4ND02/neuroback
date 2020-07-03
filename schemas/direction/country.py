from ma import ma
from models.direction.direction import CountryModel


class CountrySchema(ma.ModelSchema):
    class Meta:
        model = CountryModel
        dump_only = ("id",)
        include_fk = True
