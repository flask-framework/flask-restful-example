from manage import db
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    """
    用户表
    """
    __tablename__ = "wx_user"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    email = Column(String(254), nullable=True, unique=True)
    phone = Column(String(20), nullable=True, unique=True)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, onupdate=datetime.now)

    USERNAME_FILED = "username"

    @property
    def is_auth(self):
        return self._is_auth

    roles = []
    perms = []

    def check_password(self, password):
        """
        校验密码
        :param password: [str] 需要校验的密码
        :return: [boolean] True: 正确, False: 错误
        """
        return check_password_hash(self.password, password)

    def make_password(self, password):
        """
        创建经过加密的密码
        :param password: [str] 需要加密的密码
        :return: [str]
            加密之后的密码
        """
        return generate_password_hash(password=password)


class Group(db.Model):
    """
    用户分组表
    """
    __tablename__ = "wx_group"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    desc = Column(String(200), nullable=True)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, onupdate=datetime.now)


class UserGroupRelation(db.Model):
    """
    用户分组关系表
    """
    __tablename__ = "wx_user_group_relation"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    group_id = Column(Integer, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, onupdate=datetime.now)


class Perm(db.Model):
    """
    权限表
    """
    __tablename__ = "wx_perm"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    desc = Column(String(200), nullable=True)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, onupdate=datetime.now)


class GroupPermRelation(db.Model):
    """
    分组权限关系表
    """
    __tablename__ = "wx_group_perm_relation"
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, nullable=False)
    perm_id = Column(Integer, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, onupdate=datetime.now)
