class BaseConfig(object):
    """
 Base config class
 """

    DEBUG = True
    TESTING = False
    SECRET_KEY = "flaskTravisToufani2019bisa"


class ProductionConfig(BaseConfig):
    """
 Production specific config
 """

    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """
 Development environment specific configuration
 """

    DEBUG = True
    TESTING = True

