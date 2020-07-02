from flask_restful import Resource
from flask import request
import pandas as pd

from models.clinical_story.medicine_type import MedicineTypeModel
from schemas.clinical_story.medicine_type import MedicineTypeSchema

medicine_type_schema_list = MedicineTypeSchema(many=True)
medicine_type_schema = MedicineTypeSchema()

class MedicineType(Resource):
    @classmethod
    def post(cls):
        medicine_type_json = request.get_json()
        print(medicine_type_json)
        medicine_type = medicine_type_schema.load(medicine_type_json)

        medicine_type.save_to_db()

        return {"success": True, "data": medicine_type_schema.dump(medicine_type)}, 201

    @classmethod
    def get(cls):
        exams = MedicineTypeModel.get_list()

        return { "success": True, "data": medicine_type_schema_list.dump(exams) }, 200

class CreateMedication(Resource):
    @classmethod
    def post(cls):
        medicines_data = pd.read_excel('Medicamentos y principios activos.xls')
        medicines_list = []
        for index, row in medicines_data.iterrows():
            m_obj = {
                "nombre": row[medicines_data.columns[1]],
                "principio_activo": row[medicines_data.columns[2]],
                "laboratorio": row[medicines_data.columns[15]],
                "presentacion": row[medicines_data.columns[20]]
            }
            medicines_list.append(m_obj)
            medicine_obj = medicine_type_schema.load(m_obj)
            medicine_obj.save_to_db()

        medicines_obj = medicine_type_schema_list.load(medicines_list)
        return { "success": True, "data": medicines_obj }