from flask_restful.reqparse import RequestParser


def login_parser():
    parser = RequestParser()
    parser.add_argument("username", type=str, required=True)
    parser.add_argument("password", type=str, required=True)
    return parser


def get_permissions_parser():
    parser = RequestParser()
    parser.add_argument("group_ids", action="append", required=True)
    return parser


def update_create_user_info_parser():
    parser = RequestParser()
    parser.add_argument("fullname", type=str, required=True)
    parser.add_argument("email", type=str, required=True)
    parser.add_argument("phone", type=str, required=True)
    parser.add_argument("role_ids", action="append", required=False)
    return parser
