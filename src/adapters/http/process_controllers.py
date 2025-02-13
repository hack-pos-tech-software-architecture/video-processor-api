from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required


bp = Blueprint("process_api", __name__)


@bp.route(
    "/processes/<process_id>/subprocesses",
    methods=["POST"],
    endpoint="register_subprocess",
)
@jwt_required()
def register_subprocess(process_id: int):
    return jsonify({"register_subprocess": "Ok"}), HTTPStatus.CREATED


@bp.route(
    "/processes/<process_id>/subprocesses/<subprocess_id>/items",
    methods=["POST"],
    endpoint="register_subprocess_items",
)
@jwt_required()
def register_subprocess_items(process_id: int, subprocess_id: int):
    return jsonify({"register_subprocess_items": "Ok"}), HTTPStatus.CREATED
