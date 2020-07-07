from flask_restful import Resource
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required,
    get_raw_jwt,
)

from utils.custom_errors import ResourceAlreadyExists, ResourceNotFound, InvalidCredentials, NotAuthorized
from db import db

from models.user import UserModel
from models.clinical_story.clinical_story import ClinicalStoryModel
from models.pacient.pacient import PacientModel
from models.news import NewsModel

from schemas.user import UserSchema
from schemas.clinical_story.clinical_story import ClinicalStorySchema
from schemas.pacient.pacient import PacientSchema
from schemas.news import NewsSchema

user_schema = UserSchema(many=True)
pacient_schema = PacientSchema(many=True)
clinical_story_schema = ClinicalStorySchema(many=True)
news_schema = NewsSchema(many=True)

class Admin(Resource):
    @classmethod
    @jwt_required
    def get(cls):
        user_id = get_jwt_identity()

        if user_id != 1:
            raise NotAuthorized

        users = UserModel.get_list([])
        users = user_schema.dump(users)
        pacients = PacientModel.get_list([])
        pacients = pacient_schema.dump(pacients)
        clinical_stories = ClinicalStoryModel.get_list([])
        clinical_stories = clinical_story_schema.dump(clinical_stories)
        news = NewsModel.get_list([])
        news = news_schema.dump(news)

        data = {
            "users": users,
            "pacients": pacients,
            "clinical_stories": clinical_stories,
            "news":  news
        }

        return { "success": True, "data": data }, 200

        