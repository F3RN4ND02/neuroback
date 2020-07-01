from ma import ma
from models.chat.chat import ChatModel


class ChatSchema(ma.ModelSchema):
    class Meta:
        model = ChatModel
        dump_only = ("id",)
        include_fk = True