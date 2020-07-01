from db import Column, Integer, ForeignKey, String, Boolean, session, Float

from .exam_result import ExamResultModel
from .medicine import MedicineModel
from .symptom import SymptomModel
from models.user import UserModel

from models.abstract_models import TimeBasedModel

class ClinicalStoryModel(TimeBasedModel):
    __tablename__ = "historias_clinicas"

    user_id = Column("usuarios_id", Integer, ForeignKey('users.id'))
    pacient_id = Column("pacientes_id", Integer, ForeignKey('pacients.id'))
    description = Column("motivo_consulta", String(200), nullable=False)
    cognitions = Column("rasgos_cognitivos", String(200), nullable=False)
    sistolic = Column("sistolica", Integer)
    diastolic = Column("diastolica", Integer)
    pulse = Column("pulso", Integer)
    resp_freq = Column("freq_respiratoria", Integer)
    temp = Column("temp", Float)
    diagnosis = Column("diagnostico", String(4))
    ord_exam =  Column("ord_exam", String(100))
    exam_result = Column("exam_result", String(100))


    def update(self, new_values) -> None:
        for key, value in new_values.items():
            setattr(self, key, value)
        session.commit()

    @classmethod
    def find_by_user_id(cls, user_id: str) -> "ClinicalStoryModel":
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def find_by_pacient_id(cls, pacient_id: str) -> "ClinicalStoryModel":
        return cls.query.filter_by(pacient_id=pacient_id).all()

    @classmethod
    def get_list(cls, query_params) -> "ClinicalStoryModel":
        query = cls.query

        if "sistolic" in query_params:
            query = query.filter_by(sistolic=query_params["sistolic"])

        if "diastolic" in query_params:
            query = query.filter_by(diastolic=query_params["diastolic"])

        if "pulse" in query_params:
            query = query.filter_by(pulse=query_params["pulse"])

        if "resp_freq" in query_params:
            query = query.filter_by(resp_freq=query_params["resp_freq"])

        if "temp" in query_params:
            query = query.filter_by(temp=query_params["temp"])
