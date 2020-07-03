from db import Column, Integer, String, ForeignKey, relationship

from models.abstract_models import BaseModel

class DirectionModel(BaseModel):
    __tablename__ = "direcciones"

    municipality_id = Column("municipios_id", Integer, ForeignKey('municipios.id'))
    description = Column("detalle", String(100))

    def __init__(self, municipality_id, description):
        self.municipality_id = municipality_id
        self.description = description

class MunicipalityModel(BaseModel):
    __tablename__ = "municipios"

    state_id = Column("estado_id", Integer, ForeignKey('estados.id'))
    name = Column("nombre", String(100), nullable=False)


    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id

class StateModel(BaseModel):
    __tablename__ = "estado"

    country_id = Column("pais_id", Integer, ForeignKey('paises.id'))
    name = Column("nombre", String(100), nullable=False)


    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id

class CountryModel(BaseModel):
    __tablename__ = "pais"

    country_name = Column("nombre", String(50), unique=True, nullable=False)


    def __init__(self, country_code, country_name):
        self.country_code = country_code
        self.country_name = country_name

    @classmethod
    def find_by_code(cls, code: str) -> "CountryModel":
        return cls.query.filter_by(country_code=code).first()