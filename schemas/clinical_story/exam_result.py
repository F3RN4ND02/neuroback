from ma import ma
from models.clinical_story.exam_result import ExamResultModel


class ExamResultSchema(ma.ModelSchema):
    class Meta:
        model = ExamResultModel
        dump_only = ("id",)
        load_only = ("date",)
        include_fk = True