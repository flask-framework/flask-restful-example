from flask_restful import Resource
from utils.resource import LoginResource
from user import dbi
from user import validator
from user import exception
from utils.errcode import ErrCode


class Login(Resource):

    def post(self):
        parser = validator.login_parser()
        args = parser.parse_args()
        username = args.get("username")
        password = args.get("password")
        try:
            user = dbi.select_user_by_username(username=username)
            if user.check_password(password=password):
                ret = {
                    "code": ErrCode.ERR_OK,
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
