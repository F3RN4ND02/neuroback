from .abstract_models import DescriptionBasedModel

class ExamTypeModel(DescriptionBasedModel):
    __tablename__ = "exam_types"

    def __init__(self, description, name):
        self.description = description
        self.name = name