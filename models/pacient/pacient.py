from db import Column, Integer, ForeignKey, Enum, Date, String, session

from models.abstract_models import TimeBasedModel

class PacientModel(TimeBasedModel):
    __tablename__ = "pacientes"

    current_direction = Column("direccion_actual", Integer, ForeignKey('direcciones.id'))
    birth_direction = Column("direccion_nacimiento", Integer, ForeignKey('direcciones.id'))
    first_name = Column("nombre", String(12), nullable=False)
    second_name = Column("segundo_nombre", String(12))
    last_name = Column("apellido", String(12), nullable=False)
    second_last_name = Column("segundo_apellido", String(12))
    document = Column("documento", String(16), nullable=False, unique=True)
    gender = Column("sexo", Enum('m', 'f', 'o'), nullable=False)
    birth_date = Column("fecha_nacimiento", Date)
    marital_status = Column("estado_civil", Enum('soltero', 'casado', 'divorciado', 'viudo'), nullable=False)
    blood_type = Column("tipo_sangre", Enum('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-', 'DESCONOCIDO'), nullable=False)
    telephone_1 = Column("telefono", String(20))
    telephone_2 = Column("telefono2", String(20))
    img_url = Column(String(200))

    @classmethod
    def find_by_document(cls, document: str) -> "PacientModel":
        return cls.query.filter_by(document=document).first()

    @classmethod
    def get_list(cls, query_params) -> "PacientModel":
        query = cls.query

        if "first_name" in query_params:
            query = query.filter_by(first_name=query_params["first_name"])

        if "second_name" in query_params:
            query = query.filter_by(second_name=query_params["second_name"])

        if "last_name" in query_params:
            query = query.filter_by(last_name=query_params["last_name"])

        if "second_last_name" in query_params:
            query = query.filter_by(second_last_name=query_params["second_last_name"])

        if "gender" in query_params:
            query = query.filter_by(gender=query_params["gender"])

        if "blood_type" in query_params:
            query = query.filter_by(blood_type=query_params["blood_type"])

        if "marital_status" in query_params:
            query = query.filter_by(marital_status=query_params["marital_status"])


        return query.all()

    def update(self, new_values) -> None:
        for key, value in new_values.items():
            setattr(self, key, value)
        session.commit()

