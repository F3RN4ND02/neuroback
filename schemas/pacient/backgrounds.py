from ma import ma
from models.pacient.backgrounds import BackgroundModel


class BackgroundSchema(ma.ModelSchema):
    class Meta:
        model = BackgroundModel
        dump_only = ("id",)