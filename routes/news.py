from resources.news import News, NewsImageUpload, New

def init_news_routes(api):
    api.add_resource(News, "/news")
    api.add_resource(New, "/news/<int:news_id>")
    api.add_resource(NewsImageUpload, "/news/<int:news_id>/image")