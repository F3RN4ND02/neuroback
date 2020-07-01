from db import Column, String, Date, Boolean, Enum, session

from .abstract_models import TimeBasedModel 


class UserModel(TimeBasedModel):
    __tablename__ = "usuarios"

    email = Column(String(40), nullable=False, unique=True)
    password = Column("contrasena", String(80), nullable=False)
    username = Column(String(20), unique=True)
    first_name = Column("nombre", String(20), nullable=False)
    last_name = Column("apellido", String(20), nullable=False)
    role = Column("rol", Enum('doctor', 'researcher'), nullable=False)
    title = Column("titulo",String(20), nullable=False)
    document = Column("documento", String(16), nullable=False, unique=True)
    college_number = Column("numero_colegio", String(40))
    doctor_number = Column("numero_medico", String(40))
    gender = Column("sexo", Enum('m', 'f', 'o'), nullable=False)
    birth_date = Column("fecha_nacimiento", Date)
    img_url = Column(String(200))
    active = Column("activo", Boolean, server_default='False')

    def __init__(self, email, password, username, first_name, last_name, role, title, document, gender, college_number="N/A", doctor_number="N/A", img_url="N/A", birth_date=None, work_city=None):
        self.email = email
        self.password = password
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.title = title
        self.document = document
        self.college_number = college_number
        self.doctor_number = doctor_number
        self.img_url = img_url
        self.gender = gender
        self.birth_date = birth_date
        self.work_city = work_city
        self.active = True

    def deactivate(self) -> None:
        self.active = False
        session.commit()

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_document(cls, document: str) -> "UserModel":
        return cls.query.filter_by(document=document).first()

    @classmethod
    def get_list(cls, query_params) -> "UserModel":
        query = cls.query

        if "first_name" in query_params:
            print("aca ando")
            query = query.filter_by(first_name=query_params["first_name"])
            

        if "last_name" in query_params:
            query = query.filter_by(last_name=query_params["last_name"])

        if "gender" in query_params:
            query = query.filter_by(gender=query_params["gender"])

        if "role" in query_params:
            query = query.filter_by(role=query_params["role"])

        if "title" in query_params:
            query = query.filter_by(title=query_params["title"])

        if "college_number" in query_params:
            query = query.filter_by(college_number=query_params["college_number"])

        
        
        return query.all()

    def update(self, new_values) -> None:
        for key, value in new_values.items():
            setattr(self, key, value)
        session.commit()
