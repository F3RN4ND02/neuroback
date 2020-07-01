from ma import ma
from models.direction.direction import StateModel


class StateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StateModel
        dump_only = ("id",)