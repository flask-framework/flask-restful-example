from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_babel import Babel
from flask_session import Session
from flask_cors import CORS
from core.urls import Urls
from flask import make_response

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("core.settings")
    api = Api(app=app)
    Session(app=app)
    Babel(app=app)
    CORS(app=app)
    urls = Urls()
    db.init_app(app=app)
    urls.init_app(app=app, api=api)

    from utils.auth import AuthException

    @app.errorhandler(AuthException)
    def invalid_usage(error):
        response = make_response(error.message)
        response.status_code = error.status_code
        return response

    return app
