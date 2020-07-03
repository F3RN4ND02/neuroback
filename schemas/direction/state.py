from ma import ma
from models.direction.direction import StateModel


class StateSchema(ma.ModelSchema):
    class Meta:
        model = StateModel
        dump_only = ("id",)
        include_fk = True