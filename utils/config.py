from config import DATABASE_CONECTION_URI

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DATABASE_CONECTION_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'admin'
    

config = {
    'development': DevelopmentConfig
}
