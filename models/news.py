from db import Column, String, Date, Boolean, Enum, session

from .abstract_models import TimeBasedModel 

class NewsModel(TimeBasedModel):
    __tablename__ = "noticias"

    title = Column("titulo", String(100), nullable=False)
    abstract = Column("resumen", String(500), nullable=False)
    link = Column("enlace", String(200), nullable=False)
    img_url = Column(String(200))

    @classmethod
    def get_list(cls, query_params=None) -> "ExamTypeModel":
        query = cls.query

        return query.all()