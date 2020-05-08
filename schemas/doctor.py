from ma import ma
from models.doctor import DoctorModel


class DoctorSchema(ma.ModelSchema):
    class Meta:
        model = DoctorModel
        load_only = ("password",)
        dump_only = ("id","created_at","updated_at","active",)
