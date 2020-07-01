from ma import ma
from models.clinical_story.medicine_type import MedicineTypeModel


class MedicineTypeSchema(ma.ModelSchema):
    class Meta:
        model = MedicineTypeModel
        dump_only = ("id",)