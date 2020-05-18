from ma import ma
from models.profession_history.profession_history import ProfessionHistoryModel


class ProfessionHistorySchema(ma.ModelSchema):
    class Meta:
        model = ProfessionHistoryModel
        dump_only = ("id",)