from resources.clinical_story import ClinicalStories, ClinicalStory, ClinicalStoryRelatedData

def init_clinical_story_routes(api):
    api.add_resource(ClinicalStories, "/clinical_stories")
    api.add_resource(ClinicalStory, "/clinical_stories/<int:clinical_story_id>")
    api.add_resource(ClinicalStoryRelatedData, "/clinical_stories/related_data")