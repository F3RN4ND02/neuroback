from db import db

class ExamTypeModel(db.Model):
    __tablename__ = "exam_types"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    exam_type = db.Column(db.String(50), nullable=False)

    def __init__(self, description, exam_type):
        self.description = description
        self.exam_type = exam_type

    @classmethod
    def find_by_id(cls, id: int) -> "ExamTypeModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()