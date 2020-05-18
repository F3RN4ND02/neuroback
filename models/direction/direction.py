from db import Column, Integer, String ForeignKey

from models.abstract_models import BaseModel

class DirectionModel(BaseModel):
    __tablename__ = "directions"

    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'))
    municipality_id = db.Column(db.Integer, db.ForeignKey('municipalities.id'))

    def __init__(self, country_id, state_id, municipality_id):
        self.country_id = country_id
        self.state_id = state_id
        self.municipality_id = municipality_id