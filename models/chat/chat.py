from db import Model, Column, Integer, DateTime, String, session, ForeignKey

from models.abstract_models import BaseModel

class ChatModel(BaseModel):
    __tablename__ = "conversaciones"

    user_id = Column("usuarios_id", Integer, ForeignKey("usuarios.id"))
    user2_id = Column("usuarios2_id", Integer, ForeignKey("usuarios.id"))

    @classmethod
    def find_by_users(cls, user, user2):
        chat = cls.query.filter_by(user_id=user).filter_by(user2_id=user2)

        if not chat:
            chat = cls.query.filter_by(user_id=user2).filter_by(user2_id=user)

        return chat