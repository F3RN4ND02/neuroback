from models.abstract_models import DescriptionBasedModel

class BackgroundModel(DescriptionBasedModel):
    __tablename__ = "antecedentes"

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @classmethod
    def get_list(cls, query_params=None) -> "ExamTypeModel":
        query = cls.query

        return query.all()