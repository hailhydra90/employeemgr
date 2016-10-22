#default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xdfmG.L\xd0.uDcr\xe5\x91\x97\xd4\xa3o\xd8`\xafK\x85X\r'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'


class DevelopmentConfig(BaseConfig):
    DEBUG = True