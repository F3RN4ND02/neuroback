from db import Column, Integer, ForeignKey, Enum, Date, String, session

from models.abstract_models import TimeBasedModel

class PacientModel(TimeBasedModel):
    __tablename__ = "pacients"

    user_id = Column(Integer, ForeignKey('users.id'))
    gender = Column(Enum('m', 'f', 'o'))
    birth_date = Column(Date, nullable=False)
    current_direction = Column(String(80))
    birth_direction = Column(String(80))
    telephone_1 = Column(String(20))
    telephone_2 = Column(String(20))

    def __init__(self, user_id, gender, birth_date, current_direction=None, birth_direction=None, telephone_1=None, telephone_2=None):
        self.user_id = user_id
        self.gender = gender
        self.birth_date = birth_date
        self.current_direction = current_direction
        self.birth_direction = birth_direction
        self.telephone_1 = telephone_1
        self.telephone_2 = telephone_2

    def update(self, new_values) -> None:
        for key, value in new_values.items():
            setattr(self, key, value)
        session.commit()

