from ma import ma
from models.chat.message import MessageModel


class MessageSchema(ma.ModelSchema):
    class Meta:
        model = MessageModel
        dump_only = ("id","date", "seen")
        include_fk = True