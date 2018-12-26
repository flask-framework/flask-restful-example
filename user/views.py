from flask_restful import Resource
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
