import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLALCHEMY_DATBASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR = os.path.join(base_dir,"../db_directory")
    SQLALCHEMY_DATBASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR,"testdb.sqlite3")
    DEBUG = True

class ProductionDevelopmentConfig(Config):
    SQLITE_DB_DIR = os.path.join(base_dir,"../db_directory")
    SQLALCHEMY_DATBASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR,"proddb.sqlite3")
    DEBUG = False