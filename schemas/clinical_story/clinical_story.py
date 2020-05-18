from ma import ma
from models.clinical_story.clinical_story import ClinicalStoryModel


class ClinicalStorySchema(ma.ModelSchema):
    class Meta:
        model = ClinicalStoryModel
        dump_only = ("id","created_at","updated_at","available")
        include_fk = True