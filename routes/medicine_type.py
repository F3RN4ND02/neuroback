from resources.medicine_type import MedicineType, CreateMedication

def init_medicines_routes(api):
    api.add_resource(MedicineType, "/medicine_types")
    api.add_resource(CreateMedication, "/create_medication")