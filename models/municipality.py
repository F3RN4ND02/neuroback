from db import db

class MunicipalityModel(db.Model):
    __tablename__ = "municipalities"

    id = db.Column(db.Integer, primary_key=True)
    municipality_name = db.Column(db.String(100), nullable=False)

    def __init__(self, municipality_name):
        self.municipality_name = municipality_name

    @classmethod
    def find_by_id(cls, id: int) -> "MunicipalityModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()