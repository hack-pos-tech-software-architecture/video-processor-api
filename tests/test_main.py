import pytest
from unittest.mock import Mock, patch
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from http import HTTPStatus


def test_flask_app_config():
    app = Flask(__name__)
    app.config["JWT_VERIFY_SUB"] = False
    app.config["JWT_SECRET_KEY"] = "test_secret_key"
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]

    jwt = JWTManager(app)

    assert app.config["JWT_VERIFY_SUB"] is False
    assert app.config["JWT_SECRET_KEY"] == "test_secret_key"
    assert app.config["JWT_TOKEN_LOCATION"] == ["headers"]


def test_flask_root_route():
    app = Flask(__name__)

    @app.get("/")
    def root():
        return jsonify({"project": "Tech Challence - Fase 5"}), HTTPStatus.OK

    client = app.test_client()
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json == {"project": "Tech Challence - Fase 5"}
