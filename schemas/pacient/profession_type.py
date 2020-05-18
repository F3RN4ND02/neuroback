from ma import ma
from models.profession_type.profession_type import ProfessionTypeModel


class ProfessionTypeSchema(ma.ModelSchema):
    class Meta:
        model = ProfessionTypeModel
        dump_only = ("id",)