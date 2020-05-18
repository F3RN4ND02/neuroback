from db import Column, Integer, ForeignKey, String, Date

from models.abstract_models import BaseModel

class ProfessionHistoryModel(BaseModel):
    __tablename__ = "profession_histories"

    profession_type_id = Column(Integer, ForeignKey('profession_types.id'))
    pacient_id = Column(Integer, ForeignKey('pacients.id'))
    description = Column(String(200), nullable=False)
    start = Column(Date)
    end = Column(Date)

    def __init__(self, profession_type_id, pacient_id, description, start=None, end=None):
        self.profession_type_id = profession_type_id
        self.pacient_id = pacient_id
        self.description = description
        self.start = start
        self.end = end