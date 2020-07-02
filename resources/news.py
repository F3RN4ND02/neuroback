from flask_restful import Resource
from flask import request
   
from models.news import NewsModel
from schemas.news import NewsSchema

news_schema_list = NewsSchema(many=True)
news_schema = NewsSchema()

class News(Resource):
    @classmethod
    def post(cls):
        news_json = request.get_json()
        print(news_json)
        news = news_schema.load(news_json)

        news.save_to_db()

        return {"success": True, "data": news_schema.dump(news)}, 201

    @classmethod
    def get(cls):
        news = NewsModel.get_list()

        return { "success": True, "data": news_schema_list.dump(news) }, 200