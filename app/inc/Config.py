import os


class BaseConfig(object):
    DEBUG  = False
    TESTING = False
    SECRET_KEY = os.urandom(16)
    
class DevelopmentConfig(BaseConfig):
    ENV = 'dev'
    DEBUG = True
    TESTING = True
    VERSIONS = 1
    MODULES = [
        'telegram'
    ]

class ProductionConfig(BaseConfig):
    ENV = 'production'
    VERSIONS = 1
    MODULES = [
        'telegram'
    ]
