from db import Column, String, Date, Boolean, Enum, session

from .abstract_models import TimeBasedModel 


class UserModel(TimeBasedModel):
    __tablename__ = "usuarios"

    email = Column(String(40), nullable=False, unique=True)
    password = Column("contrasena", String(80), nullable=False)
    username = Column(String(20), unique=True)
    first_name = Column("nombre", String(20), nullable=False)
    last_name = Column("apellido", String(20), nullable=False)
    role = Column("rol", Enum('Estudiante', 'Medico', 'Medico Especialista', 'Doctor', 'Investigador'), nullable=False)
    document = Column("documento", String(16), nullable=False, unique=True)
    gender = Column("sexo", Enum('m', 'f', 'o'), nullable=False)
    img_url = Column(String(200))
    active = Column("activo", Boolean, server_default='False')

    def __init__(self, email, password, username, first_name, last_name, role, document, gender, img_url="N/A"):
        self.email = email
        self.password = password
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.document = document
        self.img_url = img_url
        self.gender = gender
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

    

        
