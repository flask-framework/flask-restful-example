from utils.auth import get_user
from flask import abort
from functools import wraps
from utils.permission import PermList


def admin_required(f):
    """
    管理员装饰器
    :param f:
    :return:
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        user = get_user()
        if user.is_superuser:
            return f(*args, **kwargs)
        else:
            abort(403)
    return decorator


def add_user_required(f):
    """

    :param f:
    :return:
    """
    def decorator(*args, **kwargs):
        user = get_user()
        if PermList.PERM_CAN_ADD_USER in user.perms:
            return f(*args, **kwargs)
        else:
            abort(403)
    return decorator
