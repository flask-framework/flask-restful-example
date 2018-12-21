from flask_restful import Resource
from flask_login import login_required


class LoginResource(Resource):

    method_decorators = [login_required]
