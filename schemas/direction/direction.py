from ma import ma
from models.direction.direction import DirectionModel


class DirectionSchema(ma.ModelSchema):
    class Meta:
        model = DirectionModel
        dump_only = ("id",)
        include_fk = True