from db import Column, Integer, ForeignKey

from .abstract_models import BaseModel

class SymptomModel(BaseModel):
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True)
    symptom_type_id = Column(Integer, ForeignKey('symptom_types.id'))
    clinical_story_id = Column(Integer, ForeignKey('clinical_stories.id'))

    def __init__(self, symptom_type, clinical_story_id):
        self.symptom_type = symptom_type
        self.clinical_story_id = clinical_story_id
