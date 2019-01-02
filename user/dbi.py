from user.models import User, UserGroupRelation, Group, GroupPermRelation, Perm
from user import exception
from manage import db
from sqlalchemy.exc import IntegrityError


def select_user_by_username(username):
    user = User.query.filter(User.username == username).first()
    if user is None:
        raise exception.UsernameNotFound("Username not found!")
    return user


def select_group_by_user_id(user_id):
    """
    根据用户ID查找分组信息
    :param user_id: [int] 用户ID
    :return:
    """
    groups = db.session.query(Group). \
        join(UserGroupRelation, Group.id == UserGroupRelation.group_id). \
        join(User, UserGroupRelation.user_id == User.id). \
        filter(User.id == user_id).all()
    return groups


def select_perms_by_group_ids(group_ids):
    """
    根据分组信息查找权限信息
    :param group_ids: [list] 分组信息ID列表
    :return:
    """
    perms = db.session.query(Perm). \
        join(GroupPermRelation, GroupPermRelation.perm_id == Perm.id). \
        join(Group, GroupPermRelation.group_id == Group.id).filter(Group.id.in_(group_ids)).all()
    return perms


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
        # print(e)
    finally:
        db.session.close()


def select_groups_by_user_id(user_id):
    """
    根据用户ID 查询分组信息
    :param user_id: [int] 用户ID
    :return:
    """
    groups = db.session.query(Group). \
        join(UserGroupRelation, Group.id == UserGroupRelation.group_id). \
        join(User, UserGroupRelation.user_id == User.id). \
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


def select_user_list_by_page(page_size, page_num, keyword=None, role_id=None, sort_name=None, sort_order=None):
    """
    获取用户列表
    :param page_size: [int] 单页用户个数
    :param page_num: [int] 页码
    :param keyword: [str] 关键字，指用户名
    :param role_id: [int] 角色id
    :param sort_name: [str] 排序的字段名
    :param sort_order: [str] 排序方式
    :return: [list]
            用户列表
    """
    query = User.query.filter()
    if sort_name:
        if sort_order == "descending":
            query = query.order_by(db.desc(getattr(User, sort_name)))
        elif sort_order == "ascending":
            query = query.order_by(getattr(User, sort_name))
    if keyword:
        query = query.filter(User.fullname.like("%{}%".format(keyword)))
    if role_id:
        query = query.join(UserGroupRelation, User.id == UserGroupRelation.user_id).filter(
            UserGroupRelation.id == role_id)
    users = query.paginate(per_page=page_size, page=page_num, error_out=False)
    return users
