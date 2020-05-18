from ma import ma
from models.direction.state import StateModel


class StateSchema(ma.ModelSchema):
    class Meta:
        model = StateModel
        dump_only = ("id",)