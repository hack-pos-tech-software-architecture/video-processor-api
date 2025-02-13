import os
from dotenv import load_dotenv

load_dotenv()

from http import HTTPStatus
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from adapters.http import (
    auth_controllers,
    process_controllers,
    user_controllers,
    upload_controllers,
)

app = Flask("VideoProcessorAPI")

app.config["JWT_VERIFY_SUB"] = False
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
app.config["JWT_TOKEN_LOCATION"] = ["headers"]

jwt = JWTManager(app)

BASE_PATH = "/api/v1"

app.register_blueprint(auth_controllers.bp, url_prefix=BASE_PATH)
app.register_blueprint(process_controllers.bp, url_prefix=BASE_PATH)
app.register_blueprint(user_controllers.bp, url_prefix=BASE_PATH)
app.register_blueprint(upload_controllers.bp, url_prefix=BASE_PATH)


app.json.sort_keys = False

# from adapters.orm.models import UserModel, ProcessModel, SubprocessModel, SubprocessItemModel
# from adapters.orm.config import get_database
# db = get_database()

# with db:
#     db.create_tables([UserModel, ProcessModel, SubprocessModel, SubprocessItemModel])


@app.get("/")
def root():
    return jsonify({"project": "Tech Challence - Fase 5"}), HTTPStatus.OK


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
