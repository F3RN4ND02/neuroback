from db import Column, Integer, ForeignKey, String, Date

from models.abstract_models import BaseModel

from .profession_type import ProfessionTypeModel

class ProfessionHistoryModel(BaseModel):
    __tablename__ = "profesion"

    profession_type_id = Column("tipo_profesiones_id", Integer, ForeignKey(ProfessionTypeModel.id))
    pacient_id = Column("pacientes_id", Integer, ForeignKey('pacientes.id'))
    start = Column("inicio", Date)
    end = Column("fin", Date)

    def __init__(self, profession_type_id, pacient_id, start=None, end=None):
        self.profession_type_id = profession_type_id
        self.pacient_id = pacient_id
        self.start = start
        self.end = end

    @classmethod
    def find_by_pacient_id(cls, pacient_id: str) -> "ClinicalStoryModel":
        return cls.query.filter_by(pacient_id=pacient_id).all()