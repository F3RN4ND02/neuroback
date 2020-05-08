from sqlalchemy.sql import func
from db import db


class ClinicalStoryModel(db.Model):
    __tablename__ = "clinical_stories"

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    pacient_id = db.Column(db.Integer, db.ForeignKey('pacients.id'))
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    available = db.Column(db.Boolean, server_default='True')

    def __init__(self, doctor_id, pacient_id, title, description):
        self.doctor_id = doctor_id
        self.pacient_id = pacient_id
        self.title = title
        self.description = description
        self.available = True
    
    @classmethod
    def find_by_id(cls, _id: int) -> "ClinicalStoryModel":
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
