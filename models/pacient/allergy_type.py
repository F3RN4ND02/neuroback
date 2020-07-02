from models.abstract_models import DescriptionBasedModel

class AllergyTypeModel(DescriptionBasedModel):
    __tablename__ = "tipo_alergias"

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @classmethod
    def get_list(cls, query_params=None) -> "ExamTypeModel":
        query = cls.query

        return query.all()