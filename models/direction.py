from db import db

class DirectionModel(db.Model):
    __tablename__ = "directions"

    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'))
    municipality_id = db.Column(db.Integer, db.ForeignKey('municipalities.id'))

    def __init__(self, country_id, state_id, municipality_id):
        self.country_id = country_id
        self.state_id = state_id
        self.municipality_id = municipality_id

    @classmethod
    def find_by_id(cls, id: int) -> "DirectionModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()