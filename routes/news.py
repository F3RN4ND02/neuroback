from resources.news import News, NewsImageUpload

def init_news_routes(api):
    api.add_resource(News, "/news")
    api.add_resource(NewsImageUpload, "/news/<int:news_id>/image")