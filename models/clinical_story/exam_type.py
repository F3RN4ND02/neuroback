from models.abstract_models import DescriptionBasedModel

class ExamTypeModel(DescriptionBasedModel):
    __tablename__ = "tipo_examenes"

    @classmethod
    def get_list(cls, query_params=None) -> "ExamTypeModel":
        query = cls.query

        return query.all()