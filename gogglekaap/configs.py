import os

from dotenv import load_dotenv

load_dotenv()

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

class Config:
    """Flask Config"""
    SECRET_KEY = 'secretkey'
    SESSION_COOKIE_NAME = 'gogglekaap'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/gogglekaap?charset=utf8
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://root:password@localhost/gogglekaap?charset=utf8')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'
    USER_STATIC_BASE_DIR = 'user_images'

    # def __init__(self):
    #     # db_env = os.environ.get('SQLALCHEMY_DATABASE_URI')
    #     db_env = os.getenv('SQLALCHEMY_DATABASE_URI')
    #     if db_env:
    #         self.SQLALCHEMY_DATABASE_URI = db_env

class DevelopmentConfig(Config):
    """Flask Config for dev"""
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    #TODO: Front 호출시 처리
    WTF_CSRF_ENABLED = False

class TestingConfig(DevelopmentConfig):
    __test__ = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_PATH, "sqlite_test.db")}'

class ProductionConfig(Config):
    pass