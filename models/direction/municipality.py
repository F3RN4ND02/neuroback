from db import Column, String

from models.abstract_models import BaseModel

class MunicipalityModel(BaseModel):
    __tablename__ = "municipalities"

    municipality_name = Column(String(100), nullable=False)

    def __init__(self, municipality_name):
        self.municipality_name = municipality_name