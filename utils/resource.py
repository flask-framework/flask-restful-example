from flask_restful import Resource
from utils.auth import jwt_required


class LoginResource(Resource):

    method_decorators = [jwt_required]
