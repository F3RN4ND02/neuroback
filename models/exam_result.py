from db import db

class ExamResultModel(db.Model):
    __tablename__ = "exam_results"

    id = db.Column(db.Integer, primary_key=True)
    exam_type_id = db.Column(db.Integer, db.ForeignKey('exam_types.id'))
    clinical_story_id = db.Column(db.Integer, db.ForeignKey('clinical_stories.id'))
    result = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, exam_type_id, clinical_story_id, result, date):
        self.exam_type_id = exam_type_id
        self.clinical_story_id = clinical_story_id
        self.result = result
        self.date = date

    @classmethod
    def find_by_id(cls, id: int) -> "ExamResultModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()