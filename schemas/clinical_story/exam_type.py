from ma import ma
from models.clinical_story.exam_type import ExamTypeModel


class ExamTypeSchema(ma.ModelSchema):
    class Meta:
        model = ExamTypeModel
        dump_only = ("id",)