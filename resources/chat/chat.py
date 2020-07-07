from flask_restful import Resource
from flask import request
   
from models.chat.chat import ChatModel
from schemas.chat.chat import ChatSchema

from models.chat.message import MessageModel
from schemas.chat.message import MessageSchema

from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required,
    get_raw_jwt,
)

from utils.custom_errors import ResourceAlreadyExists, ResourceNotFound, InvalidCredentials, NotAuthorized

chat_schema = ChatSchema()
chat_schema_list = ChatSchema(many=True)
message_schema_list = MessageSchema(many=True)

class Chats(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        chat_json = request.get_json()
        chat = chat_schema.load(chat_json)

        chat.save_to_db()

        return {"success": True, "data": chat_schema.dump(chat)}, 201

    @classmethod
    @jwt_required
    def get(cls):
        user_id = get_jwt_identity()
        chats = ChatModel.find_by_single_users(user_id)

        chats = chat_schema_list.dump(chats)

        return {"success": True, "data": chats}, 200


class Chat(Resource):
    @classmethod
    @jwt_required
    def get(cls, chat_id: int):
        chat = ChatModel.find_by_id(chat_id)
        if not chat:
            raise ResourceNotFound

        chat = chat_schema.dump(chat)

        messages = MessageModel.find_by_chat_id(chat_id)

        chat['messages'] = message_schema_list.dump(messages)
        
        return { "success": True, "data": chat }, 200
