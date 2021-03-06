from ma import ma
from models.pacient.profession_history import ProfessionHistoryModel


class ProfessionHistorySchema(ma.ModelSchema):
    class Meta:
        model = ProfessionHistoryModel
        dump_only = ("id",)
        include_fk = True