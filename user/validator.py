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
