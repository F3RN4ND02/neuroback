from ma import ma
from models.clinical_story.metadata import MetadataModel


class MetadataSchema(ma.ModelSchema):
    class Meta:
        model = MetadataModel
        dump_only = ("id",)
        include_fk = True