from db import Column, Integer, String, ForeignKey

from models.abstract_models import BaseModel

class FamilyBackgroundModel(BaseModel):
    __tablename__ = "antecedentes_familiares"

    family_background_type_id = Column("antecedentes_id", Integer, ForeignKey('antecedentes.id'))
    pacient_id = Column("pacientes_id", Integer, ForeignKey('pacientes.id'))
    family_member = Column("familiar", String(40))

    @classmethod
    def find_by_pacient_id(cls, pacient_id: str) -> "ClinicalStoryModel":
        return cls.query.filter_by(pacient_id=pacient_id).all()