from ma import ma
from models.pacient.allergy import AllergyModel


class AllergySchema(ma.ModelSchema):
    class Meta:
        model = AllergyModel
        dump_only = ("id",)
        include_fk = True