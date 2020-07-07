from db import Model, Column, Integer, DateTime, String, session, ForeignKey

from models.abstract_models import BaseModel

class ChatModel(BaseModel):
    __tablename__ = "conversaciones"

    user_id = Column("usuarios_id", Integer, ForeignKey("usuarios.id"))
    user2_id = Column("usuarios2_id", Integer, ForeignKey("usuarios.id"))

    @classmethod
    def find_by_users(cls, user, user2):
        chat = cls.query.filter_by(user_id=user).filter_by(user2_id=user2).first()

        if not chat:
            chat = cls.query.filter_by(user_id=user2).filter_by(user2_id=user).first()

        return chat

    @classmethod
    def find_by_single_user(cls, user_id):
        chatsUser1 = cls.query.filter_by(user_id=user_id).all()
        chatUser2 = cls.query.filter_by(user2_id=user_id).all()

        chat_mix = chatsUser1
        
        for chat in chatUser2:
            if chat_mix.count(chat) == 0:
                chat_mix.append(chat)

        return chat_mix