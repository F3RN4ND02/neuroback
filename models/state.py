from db import db

class StateModel(db.Model):
    __tablename__ = "states"

    id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(100), nullable=False)

    def __init__(self, state_name):
        self.state_name = state_name

    @classmethod
    def find_by_id(cls, id: int) -> "StateModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
