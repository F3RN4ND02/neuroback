from flask_restful import Resource
from flask import request
   
from models.clinical_story.exam_type import ExamTypeModel
from schemas.clinical_story.exam_type import ExamTypeSchema

exam_type_schema_list = ExamTypeSchema(many=True)
exam_type_schema = ExamTypeSchema()

class ExamTypes(Resource):
    @classmethod
    def post(cls):
        exam_type_json = request.get_json()
        print(exam_type_json)
        exam_type = exam_type_schema.load(exam_type_json)

        exam_type.save_to_db()

        return {"success": True, "data": exam_type_schema.dump(exam_type)}, 201

    @classmethod
    def get(cls):
        exams = ExamTypeModel.get_list()

        return { "success": True, "data": exam_type_schema_list.dump(exams) }, 200