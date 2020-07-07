from flask_restful import Resource
from flask import request
   
from models.news import NewsModel
from schemas.news import NewsSchema

from datetime import datetime 
from werkzeug.utils import secure_filename

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

class New(Resource):
    @classmethod
    def put(cls, news_id):
        news = NewsModel.find_by_id(news_id)
        if not news:
            raise ResourceNotFound

        fields_json = request.get_json()

        news.update(fields_json)
        return { "success": True, "data": news_schema.dump(news) }, 200

class NewsImageUpload(Resource):
    @classmethod
    def post(cls, news_id):
        str_time = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]
        f = request.files['image']
        f_name = str_time + secure_filename(f.filename)
        file_name = os.path.join("./static/" + f_name)
        f.save(file_name)


        news = NewsModel.find_by_id(news_id)

        news.img_url = file_name

        news.save_to_db()
        
        return { "success": True, "data": file_name }, 200 