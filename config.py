class Config(object):
    DEBUG = True
    TESTING = False
    SESSION_TYPE = 'filesystem'

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SESSION_TYPE = 'filesystem'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True