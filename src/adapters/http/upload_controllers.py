import os

from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from adapters.aws.s3 import StorageS3
from adapters.orm.repositories import ProcessRepository, UserRepository
from domain.services import ProcessService

service = ProcessService(UserRepository(), ProcessRepository(), StorageS3())


bp = Blueprint("upload_api", __name__)


@bp.route("/upload", methods=["POST"], endpoint="upload_files")
@jwt_required()
def upload_files():
    user = get_jwt_identity()

    if "files" not in request.files:
        return jsonify({"error": "No files part in the request"}), 400

    files = request.files.getlist("files")
    service.upload_multiple_files(files=files, user_id=1)

    return jsonify({"upload_files": "ok"}), 200
