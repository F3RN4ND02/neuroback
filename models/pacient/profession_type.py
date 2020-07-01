from models.abstract_models import DescriptionBasedModel

class ProfessionTypeModel(DescriptionBasedModel):
    __tablename__ = "tipo_profesiones"

    def __init__(self, name, description):
        self.name = name
        self.description = description