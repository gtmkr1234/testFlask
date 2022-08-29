import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from applicatin.database import db


app=None

def create_app:
    app = Flask(__name__,template_folder="templates")
    if(os.getenv('ENV',"development"))