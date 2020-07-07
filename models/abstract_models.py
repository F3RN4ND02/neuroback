from sqlalchemy.sql import func
from db import Model, Column, Integer, DateTime, String, session

class BaseModel(Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True)

    @classmethod
    def find_by_id(cls, id: int):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self) -> None:
        session.add(self)
        session.commit()


class TimeBasedModel(BaseModel):
    __abstract__ = True
    created_at = Column("creado_en", DateTime, server_default=func.now())
    updated_at = Column("actualizado_en", DateTime, server_default=func.now(), onupdate=func.now())

class DescriptionBasedModel(BaseModel):
    __abstract__ = True
    name = Column("nombre", String(200), nullable=False)
    description = Column("descripcion", String(600), nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()