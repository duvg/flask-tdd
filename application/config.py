import os

class Config(object):
    """Base Configuration"""
    db_user = os.environ["POSTGRES_USER"]
    db_password = os.environ["POSTGRES_PASSWORD"]
    db_hostname = os.environ["POSTGRES_HOSTNAME"]
    db_port = os.environ["POSTGRES_PORT"]
    database_name = os.environ["APPLICATION_DB"]
    
    
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_hostname}:{db_port}/{database_name}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production configuration"""


class DevelopmentConfig(Config):
    """Development configuration"""


class TestingConfig(Config):
    """Testing configuration"""
    
    TESTING = True
