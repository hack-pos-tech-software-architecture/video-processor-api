from http import HTTPStatus
from flask import Blueprint, request, jsonify

from adapters.orm.repositories import UserRepository
from adapters.security.bcrypt import HashBcrypt
from domain.exceptions import UserAlreadyExistsException
from domain.services import UserService

service = UserService(UserRepository(), HashBcrypt())

bp = Blueprint("user_api", __name__)


@bp.route(
    "/users",
    methods=["POST"],
    endpoint="register_user",
)
def register_user():
    try:
        data = request.get_json()
        service.register_user(data.get("username"), data.get("password"))
        return jsonify({"message": "User created"}), HTTPStatus.CREATED
    except UserAlreadyExistsException as err:
        return jsonify({"message": str(err)}), HTTPStatus.BAD_REQUEST
    except Exception as err:
        return jsonify({"message": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR
