from flask import request
import jwt
import datetime
from functools import wraps
from user.models import User
from flask import session
from core.settings import JWT_EXPIRED, SECRET_KEY
from utils.exception import AuthException


def general_token(user):
    """
    生成token
    :param user: [object User] 用户数据对象
    :return: [str]
        加密字符串
    """
    expire_time = datetime.datetime.utcnow() + JWT_EXPIRED
    secret_key = SECRET_KEY
    if hasattr(user, User.USERNAME_FILED):
        username = getattr(user, User.USERNAME_FILED)
        payload = {
            "exp": expire_time,
            "id": user.id,
            "username": username
        }
        return jwt.encode(payload=payload, key=secret_key)
    else:
        raise jwt.exceptions.InvalidKeyError


def decode_token(token):
    secret_key = SECRET_KEY
    return jwt.decode(jwt=token, key=secret_key)


def jwt_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            auth_token = request.headers.get("Auth-Token", None)
            if auth_token is not None:
                payload = decode_token(auth_token)
                if "auth_user" in session:
                    user = session["auth_user"]
                    if hasattr(user, User.USERNAME_FILED) and hasattr(user, "id"):
                        username = getattr(user, User.USERNAME_FILED)
                        user_id = getattr(user, "id")
                        if payload.get("id") == user_id and payload.get("username") == username:
                            return f(*args, **kwargs)
                        else:
                            raise AuthException(status_code=401, message="token user information invalid!")
                    else:
                        AuthException(status_code=401, message="token has invalid user information!")
                else:
                    raise AuthException(status_code=401, message="token has no user information!")
            else:
                raise AuthException(status_code=401, message="token empty!")
        except jwt.exceptions.DecodeError:
            raise AuthException(status_code=401, message="invalid token!")
        except jwt.exceptions.ExpiredSignature:
            raise AuthException(status_code=401, message="token has expired!")
    return decorator


def login_user(user):
    """

    :param user:
    :return:
    """
    session["auth_user"] = user


def logout():
    del session["auth_user"]


def get_user():
    return session["auth_user"]
