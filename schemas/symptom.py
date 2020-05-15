from ma import ma
from models.symptom import SymptomModel


class SymptomSchema(ma.ModelSchema):
    class Meta:
        model = SymptomModel
        dump_only = ("id",)