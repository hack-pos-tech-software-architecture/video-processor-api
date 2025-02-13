from http import HTTPStatus
from flask import Blueprint, request, jsonify

from adapters.orm.repositories import UserRepository
from adapters.security.bcrypt import HashBcrypt
from adapters.security.jwt import AccessTokenJWT
from domain.exceptions import NotAuthorizedException
from domain.services import AuthService

service = AuthService(UserRepository(), HashBcrypt(), AccessTokenJWT())

bp = Blueprint("auth_api", __name__)


@bp.route(
    "/auth/login",
    methods=["POST"],
    endpoint="auth_login",
)
def auth_login():
    try:
        data = request.get_json()
        token = service.login(data.get("username"), data.get("password"))
        return jsonify({"message": "Login Success", "access_token": token})
    except NotAuthorizedException as err:
        return jsonify({"message": str(err)}), HTTPStatus.UNAUTHORIZED
    except Exception as err:
        return jsonify({"message": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR
