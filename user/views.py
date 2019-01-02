from flask_restful import Resource
from flask import request
from flask_restful.fields import _iso8601
from utils.resource import LoginResource
from user import dbi
from user import validator
from user import exception
from utils.errcode import ErrCode
from utils.auth import login_user, general_token, get_user, logout


class Login(Resource):

    def post(self):
        parser = validator.login_parser()
        args = parser.parse_args()
        username = args.get("username")
        password = args.get("password")
        try:
            user = dbi.select_user_by_username(username=username)
            if user.check_password(password=password):
                # 查找分组信息
                group_list = dbi.select_group_by_user_id(user_id=user.id)
                for group in group_list:
                    if group.name not in user.roles:
                        user.roles.append(group.name)
                # 查找权限信息
                perm_list = dbi.select_perms_by_group_ids(group_ids=user.roles)
                for perm in perm_list:
                    if perm.name not in user.perms:
                        user.perms.append(perm.name)
                login_user(user)
                token = general_token(user)
                ret = {
                    "code": ErrCode.ERR_OK,
                    "token": token.decode(),
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "is_active": user.is_active,
                        "is_superuser": user.is_superuser,
                        "roles": user.roles,
                        "perms": user.perms,
                    },
                    "message": "Login success!"
                }
                return ret
            else:
                ret = {
                    "code": ErrCode.ERR_PASSWORD_ERROR,
                    "message": "Password error!"
                }
                return ret
        except exception.UsernameNotFound:
            ret = {
                "code": ErrCode.ERR_USERNAME_NOT_FOUND,
                "message": "Username not found!"
            }
            return ret


class GetGroupsByUser(LoginResource):

    def get(self, user_id):
        try:
            groups = dbi.select_groups_by_user_id(user_id=user_id)
            group_list = []
            for group in groups:
                group_list.append({
                    "id": group.id,
                    "name": group.name,
                })
            ret = {
                "code": ErrCode.ERR_OK,
                "message": "Get groups information success!",
                "groups": group_list
            }
            return ret
        except Exception as e:
            ret = {
                "code": ErrCode.ERR_UNKNOWN,
                "message": str(e)
            }
            return ret


class GetPermissionsByGroup(LoginResource):

    def get(self):
        parser = validator.get_permissions_parser()
        args = parser.parse_args()
        group_ids = args.get("group_ids")
        try:
            perms = dbi.select_permissions_by_group_ids(group_ids=group_ids)
            perm_list = []
            for perm in perms:
                perm_list.append({
                    "id": perm.id,
                    "name": perm.name
                })
            ret = {
                "code": ErrCode.ERR_OK,
                "message": "Get permissions success!",
                "permissions": perm_list
            }
            return ret
        except Exception as e:
            ret = {
                "code": ErrCode.ERR_UNKNOWN,
                "message": str(e)
            }
            return ret


class GetSefProfile(LoginResource):

    def get(self):
        user = get_user()
        print(user)


class Logout(LoginResource):

    def get(self):
        logout()
        ret = {
            "code": ErrCode.ERR_OK,
            "message": "Logout user success!"
        }
        return ret


class UserList(LoginResource):
    """
    获取用户列表，可以使用关键字和角色ID搜索
    """

    def get(self):
        keyword = request.args.get("keyword", None)
        role_id = request.args.get("role_id", None)
        sort_name = request.args.get("sort_name", None)
        sort_order = request.args.get("sort_order", None)
        try:
            page_num = int(request.args.get("page", 1))
            page_size = int(request.args.get("page_size", 20))
        except (TypeError, ValueError):
            # 传入的参数不是int数据
            page_num = 1
            page_size = 20
        user_list = []
        info_list = dbi.select_user_list_by_page(page_num=page_num, page_size=page_size, keyword=keyword,
                                                 role_id=role_id, sort_name=sort_name, sort_order=sort_order)
        for user in info_list.items:
            roles = dbi.select_groups_by_user_id(user_id=user.id)
            role_list = []
            for role in roles:
                role_list.append(role.name)
            user_list.append({
                "id": user.id,
                "username": user.username,
                # "fullname": user.fullname,
                "email": user.email,
                "phone": user.phone,
                "is_active": user.is_active,
                "is_superuser": user.is_superuser,
                "roles": ",".join(role_list),
                # "create_at": _iso8601(user.create_at),
                # "update_at": _iso8601(user.update_at),
            })
        msg = {
            "code": ErrCode.ERR_OK,
            "message": "Get user list success",
            "users": user_list,
            "pages": info_list.pages,
            "total": info_list.total
        }
        return msg
