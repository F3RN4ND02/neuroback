from db import db

class CountryModel(db.Model):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(2), primary_key=True)
    country_name = db.Column(db.String(50), nullable=False)

    def __init__(self, country_code, country_name):
        self.country_code = country_code
        self.country_name = country_name

    @classmethod
    def find_by_id(cls, id: int) -> "CountryModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_code(cls, code: str) -> "CountryModel":
        return cls.query.filter_by(country_code=code).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

