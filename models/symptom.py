from db import db

class SymptomModel(db.Model):
    __tablename__ = "symptoms"

    id = db.Column(db.Integer, primary_key=True)
    symptom_type_id = db.Column(db.Integer, db.ForeignKey('symptom_types.id'))
    clinical_story_id = db.Column(db.Integer, db.ForeignKey('clinical_stories.id'))

    def __init__(self, symptom_type, clinical_story_id):
        self.symptom_type = symptom_type
        self.clinical_story_id = clinical_story_id

    @classmethod
    def find_by_id(cls, id: int) -> "SymptomModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()