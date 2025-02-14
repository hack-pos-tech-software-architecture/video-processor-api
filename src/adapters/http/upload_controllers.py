import os

from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from adapters.aws.s3 import StorageS3
from adapters.aws.sqs import PublishQueueSQS
from adapters.orm.repositories import ProcessRepository, UserRepository
from domain.services import ProcessService


SQS_QUEUE_URL = (
    "https://sqs.us-east-1.amazonaws.com/442042528966/extract-frames-queue.fifo"
)
BUCKET_NAME = "video-processor-s3"

service = ProcessService(
    UserRepository(),
    ProcessRepository(),
    PublishQueueSQS(queue_url=SQS_QUEUE_URL),
    StorageS3(bucket_name=BUCKET_NAME),
)


bp = Blueprint("upload_api", __name__)


@bp.route("/upload", methods=["POST"], endpoint="upload_files")
@jwt_required()
def upload_files():
    # user = get_jwt_identity()

    if "file" not in request.files:
        return jsonify({"error": "No files part in the request"}), 400

    file = request.files.get("file")

    service = ProcessService(
        UserRepository(),
        ProcessRepository(),
        PublishQueueSQS(queue_url=SQS_QUEUE_URL),
        StorageS3(bucket_name=BUCKET_NAME),
    )

    response = service.upload_fileobj(fileobj=file, file_name=file.filename)

    return jsonify(response), HTTPStatus.CREATED
