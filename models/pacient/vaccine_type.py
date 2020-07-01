from models.abstract_models import DescriptionBasedModel

class VaccineTypeModel(DescriptionBasedModel):
    __tablename__ = "tipo_vacunas"

    def __init__(self, name, description):
        self.name = name
        self.description = description