from models.abstract_models import DescriptionBasedModel

class AllergyTypeModel(DescriptionBasedModel):
    __tablename__ = "tipo_alergias"

    def __init__(self, name, description):
        self.name = name
        self.description = description