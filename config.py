import os

class Config:
    
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key=7bd6326c2a582ce74fc3c6740d6280ec'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

@staticmethod
def init_app(app):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}