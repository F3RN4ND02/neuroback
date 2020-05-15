from ma import ma
from models.examResult import ExamResultModel


class ExamResultSchema(ma.ModelSchema):
    class Meta:
        model = ExamResultModel
        dump_only = ("id",)
        include_fk = True