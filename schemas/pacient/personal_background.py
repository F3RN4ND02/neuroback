from ma import ma
from models.pacient.personal_background import PersonalBackgroundModel


class PersonalBackgroundSchema(ma.ModelSchema):
    class Meta:
        model = PersonalBackgroundModel
        dump_only = ("id",)
        include_fk = True