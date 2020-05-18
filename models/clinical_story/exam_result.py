from db import Column, Integer, ForeignKey, String, Date

from .abstract_models import BaseModel

class ExamResultModel(BaseModel):
    __tablename__ = "exam_results"

    exam_type_id = Column(Integer, ForeignKey('exam_types.id'))
    clinical_story_id = Column(Integer, ForeignKey('clinical_stories.id'))
    result = Column(String(200), nullable=False)
    date = Column(Date, nullable=False)

    def __init__(self, exam_type_id, clinical_story_id, result, date):
        self.exam_type_id = exam_type_id
        self.clinical_story_id = clinical_story_id
        self.result = result
        self.date = date
