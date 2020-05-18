from db import Column, String, Date, Boolean, Enum, session

from .abstract_models import TimeBasedModel 


class UserModel(TimeBasedModel):
    __tablename__ = "users"

    email = Column(String(40), nullable=False, unique=True)
    password = Column(String(80), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    role = Column(Enum('doctor', 'researcher'), nullable=False)
    gender = Column(Enum('male', 'female', 'other'))
    birth_date = Column(Date)
    work_city = Column(Date)
    active = Column(Boolean, server_default='False')

    def __init__(self, email, password, first_name, last_name, role, gender, birth_date=None, work_city=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.gender = gender
        self.birth_date = birth_date
        self.work_city = work_city
        self.active = False

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        return cls.query.filter_by(email=email).first()
    
    def update(self, new_values) -> None:
        for key, value in new_values.items():
            setattr(self, key, value)
        session.commit()
