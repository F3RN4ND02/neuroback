from .abstract_models import DescriptionBasedModel

class SymptomTypeModel(DescriptionBasedModel):
    __tablename__ = "symptom_types"

    def __init__(self, name, description):
        self.name = name
        self.description = description