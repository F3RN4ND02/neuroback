from models.abstract_models import DescriptionBasedModel

class ProfessionTypeModel(DescriptionBasedModel):
    __tablename__ = "profession_types"

    def __init__(self, name, description):
        self.name = name
        self.description = description