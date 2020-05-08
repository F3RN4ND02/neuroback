from sqlalchemy.sql import func
from db import db


class DoctorModel(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)
    work_city = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    active = db.Column(db.Boolean, server_default='False')

    def __init__(self, email, password, first_name, last_name, birth_date=None, work_city=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.work_city = work_city
        self.active = False

    @classmethod
    def find_by_email(cls, email: str) -> "DoctorModel":
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_by_id(cls, _id: int) -> "DoctorModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def update(self, new_values) -> None:
        for key, value in new_values.items():
            setattr(self, key, value)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
