from db import Column, Integer, ForeignKey, Boolean

from models.abstract_models import BaseModel

from models.clinical_story.medicine_type import MedicineTypeModel

class MedicineModel(BaseModel):
    __tablename__ = "medicaciones"

    medicine_type_id = Column("medicamentos_id", Integer, ForeignKey(MedicineTypeModel.id))
    clinical_story_id = Column("historias_clinicas_id", Integer, ForeignKey('historias_clinicas.id'))
    background = Column("antecedente", Boolean)

    @classmethod
    def get_list(cls, query_params=None) -> "ExamTypeModel":
        query = cls.query

        return query.all()