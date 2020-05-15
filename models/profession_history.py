from db import db

class ProfessionHistoryModel(db.Model):
    __tablename__ = "profession_histories"

    id = db.Column(db.Integer, primary_key=True)
    profession_type_id = db.Column(db.Integer, db.ForeignKey('profession_types.id'))
    pacient_id = db.Column(db.Integer, db.ForeignKey('pacients.id'))
    description = db.Column(db.String(200), nullable=False)
    start = db.Column(db.Date)
    end = db.Column(db.Date)

    def __init__(self, description):
        self.description = description

    @classmethod
    def find_by_id(cls, id: int) -> "ProfessionHistoryModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()