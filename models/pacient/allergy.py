from db import Column, Integer, ForeignKey

from models.abstract_models import BaseModel

class AllergyModel(BaseModel):
    __tablename__ = "allergies"

    allergy_type_id = Column(Integer, ForeignKey('allergy_types.id'))
    pacient_id = Column(Integer, ForeignKey('pacients.id'))

    def __init__(self, allergy_type, pacient_id):
        self.allergy_type = allergy_type
        self.pacient_id = pacient_id