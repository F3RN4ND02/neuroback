from db import Column, String

from models.abstract_models import BaseModel

class StateModel(BaseModel):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    state_name = Column(String(100), nullable=False)

    def __init__(self, state_name):
        self.state_name = state_name
