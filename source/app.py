from flask import Flask
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from constants import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)


class Application:
    def __init__(self):
        self.app = app
        self.app.DEBUG = True
        self.sqlalchemy = create_engine(SQLALCHEMY_DATABASE_URI)
        self.session = sessionmaker(bind=self.sqlalchemy)()
        self.client = MongoClient()
        self.db = self.client.currency
        self.posts = self.db.posts

    def start(self):
        import urls
        urls.registration_api(self.app)


application = Application()
application.start()
