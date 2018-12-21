from flask_login import current_user
from flask import abort
from functools import wraps


def admin_required(f):
    """
    管理员装饰器
    :param f:
    :return:
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        if current_user.is_superuser:
            return f(*args, **kwargs)
        else:
            abort(403)
    return decorator
