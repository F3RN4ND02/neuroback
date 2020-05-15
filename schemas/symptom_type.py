from ma import ma
from models.symptom_type import SymptomTypeModel


class SymptomTypeSchema(ma.ModelSchema):
    class Meta:
        model = SymptomTypeModel
        dump_only = ("id",)