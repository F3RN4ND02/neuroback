from db import Column, Integer, ForeignKey, String, Date

from models.abstract_models import BaseModel

from models.clinical_story.exam_type import ExamTypeModel

class ExamResultModel(BaseModel):
    __tablename__ = "examenes"

    exam_type_id = Column("type_exam_id", Integer, ForeignKey(ExamTypeModel.id))
    clinical_story_id = Column("entradas_id", Integer, ForeignKey('historias_clinicas.id'))
    result = Column("resultado", String(200), nullable=False)
    date = Column(Date, nullable=False)

    def __init__(self, exam_type_id, clinical_story_id, result, date):
        self.exam_type_id = exam_type_id
        self.clinical_story_id = clinical_story_id
        self.result = result
        self.date = date

    @classmethod
    def find_by_exam_type_id(cls, exam_type_id: str) -> "ExamResultModel":
        return cls.query.filter_by(exam_type_id=exam_type_id).all()
