from ma import ma
from models.examType import ExamTypeModel


class ExamTypeSchema(ma.ModelSchema):
    class Meta:
        model = ExamTypeModel
        dump_only = ("id",)