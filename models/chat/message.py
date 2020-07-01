from db import Model, Column, Integer, DateTime, String, session, ForeignKey, Boolean

from models.abstract_models import TimeBasedModel

class MessageModel(TimeBasedModel):
    __tablename__ = "mensajes"

    chat_id = Column("conversaciones_id", Integer, ForeignKey("conversaciones.id"))
    user_id = Column("usuarios_id", Integer, ForeignKey("conversaciones.id"))
    content = Column("contenido", String(500), nullable=False)
    seen = Column("leido", Boolean)
    date = Column("fecha", DateTime)