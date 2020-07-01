from flask_restful import Resource
from flask import request
   
from models.chat.chat import ChatModel
from schemas.chat.chat import ChatSchema

from models.chat.message import MessageModel
from schemas.chat.message import MessageSchema 

from utils.custom_errors import ResourceAlreadyExists, ResourceNotFound, InvalidCredentials, NotAuthorized

chat_schema = ChatSchema()
message_schema_list = MessageSchema(many=True)

class Chats(Resource):
    @classmethod
    def post(cls):
        chat_json = request.get_json()
        chat = chat_schema.load(chat_json)

        chat.save_to_db()

        return {"success": True, "data": chat_schema.dump(chat)}, 201

class Chat(Resource):
    @classmethod
    def get(cls, chat_id: int):
        chat = ChatModel.find_by_id(chat_id)
        if not chat:
            raise ResourceNotFound

        chat = chat_schema.dump(chat)

        messages = MessageModel.find_by_chat_id(chat_id)

        chat['messages'] = message_schema_list.dump(messages)
        
        return { "success": True, "data": chat }, 200
