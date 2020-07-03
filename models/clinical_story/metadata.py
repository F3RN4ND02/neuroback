from db import Column, Integer, ForeignKey, Boolean

from models.abstract_models import BaseModel

from models.clinical_story.metadata_type import MetadataTypeModel
class MetadataModel(BaseModel):
    __tablename__ = "metadatos"

    metadata_type_id = Column("tipo_metadatos_id", Integer, ForeignKey(MetadataTypeModel.id))
    clinical_story_id = Column("historias_clinicas_id", Integer, ForeignKey('historias_clinicas.id'))
    relevant = Column("relevante", Boolean, nullable=False)

    @classmethod
    def find_by_story_id(cls, story_id: str) -> "ExamResultModel":
        return cls.query.filter_by(clinical_story_id=story_id).all()