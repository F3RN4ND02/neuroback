from ma import ma
from models.clinical_story.metadata_type import MetadataTypeModel


class MetadataTypeSchema(ma.ModelSchema):
    class Meta:
        model = MetadataTypeModel
        dump_only = ("id",)