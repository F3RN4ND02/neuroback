from db import Column, Integer, ForeignKey, String, Boolean, session

from .abstract_models import TimeBasedModel

class ClinicalStoryModel(TimeBasedModel):
    __tablename__ = "clinical_stories"

    user_id = Column(Integer, ForeignKey('users.id'))
    pacient_id = Column(Integer, ForeignKey('pacients.id'))
    title = Column(String(80), nullable=False)
    description = Column(String(200), nullable=False)
    available = Column(Boolean, server_default='True')

    def __init__(self, doctor_id, pacient_id, title, description):
        self.doctor_id = doctor_id
        self.pacient_id = pacient_id
        self.title = title
        self.description = description
        self.available = True

    def update(self, new_values) -> None:
        for key, value in new_values.items():
            setattr(self, key, value)
        session.commit()
