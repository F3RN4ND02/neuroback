from db import db

class AllergyTypeModel(db.Model):
    __tablename__ = "allergy_types"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, description):
        self.description = description

    @classmethod
    def find_by_id(cls, id: int) -> "AllergyTypeModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()