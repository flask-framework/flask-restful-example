from user.models import User, UserGroupRelation, Group, GroupPermRelation, Perm
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


def select_groups_by_user_id(user_id):
    """
    根据用户ID 查询分组信息
    :param user_id: [int] 用户ID
    :return:
    """
    groups = db.session.query(Group).\
        join(UserGroupRelation, Group.id == UserGroupRelation.group_id).\
        join(User, UserGroupRelation.user_id == User.id).\
        filter(User.id == user_id)
    return groups


def select_permissions_by_group_ids(group_ids):
    """
    根据分组信息获取权限信息
    :param group_ids: [list] 分组ID列表
    :return:
    """
    permissions = db.session.query(Perm). \
        join(GroupPermRelation, GroupPermRelation.perm_id == Perm.id). \
        join(Group, GroupPermRelation.group_id == Group.id). \
        filter(Group.id.in_(group_ids)). \
        group_by(Perm.name)
    return permissions
