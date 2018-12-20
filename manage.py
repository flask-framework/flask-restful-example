from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_babel import Babel
from flask_session import Session
from core.urls import load_urls

# 创建app
app = Flask(__name__)

# 初始化配置
app.config.from_object("core.settings")

# 初始化db
db = SQLAlchemy(app=app)

# 初始化restful api
api = Api(app=app)
load_urls(app=app, api=api)

# 初始化翻译
babel = Babel(app)

# 初始化session
sess = Session()
sess.init_app(app=app)


if __name__ == "__main__":
    app.run()
