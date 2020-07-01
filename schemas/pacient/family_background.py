from ma import ma
from models.pacient.family_background import FamilyBackgroundModel


class FamilyBackgroundSchema(ma.ModelSchema):
    class Meta:
        model = FamilyBackgroundModel
        dump_only = ("id",)
        include_fk = True