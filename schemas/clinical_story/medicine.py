from ma import ma
from models.clinical_story.medicine import MedicineModel


class MedicineSchema(ma.ModelSchema):
    class Meta:
        model = MedicineModel
        dump_only = ("id",)
        include_fk = True