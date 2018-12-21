from user.models import User, UserGroupRelation, Group, GroupPermRelation
from user import exception
from manage import db
from sqlalchemy.exc import IntegrityError


def select_user_by_username(username):
    user = User.query.filter(User.username==username).first()
    if user is None:
        raise exception.UsernameNotFound("Username not found!")
    return user


def insert_admin_user(username, password, email, phone):
    """
    简单的插入用户，用于命令行创建admin用户
    :param username: [str] 用户名
    :param password: [str] 未加密的密码
    :return:
    """
    user = User()
    user.username = username
    user.password = user.make_password(password)
    user.email = email
    user.phone = phone
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()
