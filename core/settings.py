import os
import redis
from datetime import timedelta


INSTALL_APPS = [
    "user",
]

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = b"\x15\xb8\xa1\xc8\xcb\xf7;\xee\xb46\xc9\xaep\xadld\x8dM\xc6\xc9SV\xefO"
SQLALCHEMY_DATABASE_URI = "postgresql://wxshop:wxshop@127.0.0.1:5432/wxshop"
SQLALCHEMY_ECHO = False
SQLALCHEMY_POOL_SIZE = 200
SQLALCHEMY_TRACK_MODIFICATIONS = True

# SESSION
SESSION_COOKIE_NAME = "wxshop_session"
SESSION_TYPE = "redis"
SESSION_REDIS = redis.Redis(host="127.0.0.1", port=6379, db=5)
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

UPLOADED_FILES_DEST = os.path.join(BASE_DIR, "static/upload")
UPLOADED_FILES_URL = "/media"
UPLOADED_FILES_ALLOW = ""
UPLOADED_FILES_DENY = ""

BABEL_DEFAULT_LOCALE = "zh_Hans_CN"
BABEL_DEFAULT_TIMEZONE = "Asia/Shanghai"

PAGE_SIZE = 20

# celery
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_BACKEND_URL = "redis://127.0.0.1:6379/1"

# 认证配置
JWT_EXPIRED = timedelta(days=3)
