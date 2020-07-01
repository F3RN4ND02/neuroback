from db import Column, Integer, ForeignKey

from models.abstract_models import BaseModel

class PersonalBackgroundModel(BaseModel):
    __tablename__ = "antecedentes_personales"

    personal_background_type_id = Column("antecedentes_id", Integer, ForeignKey('antecedentes.id'))
    pacient_id = Column("pacientes_id", Integer, ForeignKey('pacientes.id'))

    def __init__(self, personal_background_type_id, pacient_id):
        self.personal_background_type_id = personal_background_type_id
        self.pacient_id = pacient_id

    @classmethod
    def find_by_pacient_id(cls, pacient_id: str) -> "ClinicalStoryModel":
        return cls.query.filter_by(pacient_id=pacient_id).all()