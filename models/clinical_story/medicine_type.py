from db import Column, String

from models.abstract_models import BaseModel

class MedicineTypeModel(BaseModel):
    __tablename__ = "medicamentos"

    nombre = Column(String(600), nullable=False)
    principio_activo = Column(String(40), nullable=False)
    laboratorio = Column(String(40), nullable=False)
    presentacion = Column(String(40))
    
    @classmethod
    def get_list(cls, query_params=None) -> "ExamTypeModel":
        query = cls.query

        return query.all()