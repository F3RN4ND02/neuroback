from db import Column, Integer, ForeignKey

from models.abstract_models import BaseModel

class VaccineModel(BaseModel):
    __tablename__ = "vacunas"

    vaccine_type_id = Column("tipo_vacunas_id", Integer, ForeignKey('tipo_vacunas.id'))
    pacient_id = Column("pacientes_id", Integer, ForeignKey('pacientes.id'))

    def __init__(self, vaccine_type_id, pacient_id):
        self.vaccine_type_id = vaccine_type_id
        self.pacient_id = pacient_id

    @classmethod
    def find_by_pacient_id(cls, pacient_id: str) -> "ClinicalStoryModel":
        return cls.query.filter_by(pacient_id=pacient_id).all()