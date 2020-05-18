from db import Column, String

from models.abstract_models import BaseModel

class CountryModel(BaseModel):
    __tablename__ = "countries"

    country_code = db.Column(db.String(2), primary_key=True)
    country_name = db.Column(db.String(50), nullable=False)

    def __init__(self, country_code, country_name):
        self.country_code = country_code
        self.country_name = country_name

    @classmethod
    def find_by_code(cls, code: str) -> "CountryModel":
        return cls.query.filter_by(country_code=code).first()