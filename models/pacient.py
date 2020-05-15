from sqlalchemy.sql import func
from db import db


class PacientModel(db.Model):
    __tablename__ = "pacients"

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    gender = db.Column(db.Enum('m', 'f', 'o'))
    birth_date = db.Column(db.Date, nullable=False)
    current_direction = db.Column(db.String(80))
    birth_direction = db.Column(db.String(80))
    telephone_1 = db.Column(db.String(20))
    telephone_2 = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, doctor_id, gender, birth_date, current_direction=None, birth_direction = None):
        self.doctor_id = doctor_id
        self.gender = gender
        self.birth_date = birth_date
        self.current_direction = current_direction
        self.birth_direction = birth_direction

    
    @classmethod
    def find_by_id(cls, _id: int) -> "PacientModel":
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
