from resources.chat.chat import Chats, Chat
from resources.chat.message import Messages

def init_chat_routes(api):
    api.add_resource(Chats, "/chats")
    api.add_resource(Chat, "/chats/<int:chat_id>")
    api.add_resource(Messages, "/messages")
