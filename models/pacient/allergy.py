from db import Column, Integer, ForeignKey

from models.abstract_models import BaseModel

class AllergyModel(BaseModel):
    __tablename__ = "alergias"

    allergy_type_id = Column(Integer, ForeignKey('tipo_alergias.id'))
    pacient_id = Column(Integer, ForeignKey('pacientes.id'))

    def __init__(self, allergy_type_id, pacient_id):
        self.allergy_type_id = allergy_type_id
        self.pacient_id = pacient_id

    @classmethod
    def find_by_pacient_id(cls, pacient_id: str) -> "ClinicalStoryModel":
        return cls.query.filter_by(pacient_id=pacient_id).all()