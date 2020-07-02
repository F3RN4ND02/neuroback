from db import Column, String

from models.abstract_models import BaseModel

class MedicineTypeModel(BaseModel):
    __tablename__ = "medicamentos"

    principio_activo = Column(String(40), nullable=False)
    laboratorio = Column(String(40), nullable=False)
    