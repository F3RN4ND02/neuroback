from resources.exam_type import ExamTypes

def init_exams_routes(api):
    api.add_resource(ExamTypes, "/exam_types")