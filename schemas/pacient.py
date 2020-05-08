from ma import ma
from models.pacient import PacientModel


class PacientSchema(ma.ModelSchema):
    class Meta:
        model = PacientModel
        dump_only = ("id","created_at","updated_at",)
        include_fk = True