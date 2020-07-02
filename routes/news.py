from resources.news import News

def init_news_routes(api):
    api.add_resource(News, "/news")