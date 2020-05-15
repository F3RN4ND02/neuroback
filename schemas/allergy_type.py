from ma import ma
from models.allergy_type import AllergyTypeModel


class AllergyTypeSchema(ma.ModelSchema):
    class Meta:
        model = AllergyTypeModel
        dump_only = ("id",)