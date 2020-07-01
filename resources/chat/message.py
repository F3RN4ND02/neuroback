from flask_restful import Resource
from flask import request
   
from models.chat.chat import ChatModel
from schemas.chat.chat import ChatSchema

from models.chat.message import MessageModel
from schemas.chat.message import MessageSchema 

from utils.custom_errors import ResourceAlreadyExists, ResourceNotFound, InvalidCredentials, NotAuthorized

chat_schema = ChatSchema()
message_schema_list = MessageSchema()

class Messages(Resource):
    @classmethod
    def post(cls):
        message_json = request.get_json()
        message = message_schema.load(message_json)

        message.save_to_db()

        return {"success": True, "data": message_schema.dump(message)}, 201