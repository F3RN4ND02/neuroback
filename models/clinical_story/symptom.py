from db import Column, Integer, ForeignKey

from models.abstract_models import BaseModel

from models.clinical_story.symptom_type import SymptomTypeModel

class SymptomModel(BaseModel):
    __tablename__ = "sintomas"

    symptom_type_id = Column("tipo_sintomas_id", Integer, ForeignKey(SymptomTypeModel.id))
    clinical_story_id = Column("historias_clinicas_id", Integer, ForeignKey('historias_clinicas.id'))


    @classmethod
    def find_by_story_id(cls, story_id: str) -> "ExamResultModel":
        return cls.query.filter_by(clinical_story_id=story_id).all()