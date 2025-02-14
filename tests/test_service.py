import pytest
from datetime import datetime
from uuid import uuid4
from unittest.mock import Mock
from domain.entities import UserEntity
from domain.exceptions import NotAuthorizedException, UserAlreadyExistsException
from domain.services import AuthService, ProcessService, UserService


def test_auth_service_login_success():
    user_repository = Mock()
    password_hash = Mock()
    access_token = Mock()

    user = UserEntity(username="testuser", password="hashedpassword")
    user_repository.get_by_username.return_value = user
    password_hash.compare_password.return_value = True
    access_token.generate_token.return_value = "generated_token"

    auth_service = AuthService(user_repository, password_hash, access_token)
    token = auth_service.login("testuser", "password")

    assert token == "generated_token"
    user_repository.get_by_username.assert_called_once_with("testuser")
    password_hash.compare_password.assert_called_once_with("password", "hashedpassword")
    access_token.generate_token.assert_called_once_with({"username": "testuser"})


def test_auth_service_login_failure():
    user_repository = Mock()
    password_hash = Mock()
    access_token = Mock()

    user_repository.get_by_username.return_value = None
    password_hash.compare_password.return_value = False

    auth_service = AuthService(user_repository, password_hash, access_token)

    with pytest.raises(NotAuthorizedException):
        auth_service.login("testuser", "wrongpassword")


def test_user_service_register_user_failure():
    user_repository = Mock()
    password_hash = Mock()

    user_repository.get_by_username.return_value = UserEntity(
        username="testuser", password="hashedpassword"
    )

    user_service = UserService(user_repository, password_hash)

    with pytest.raises(UserAlreadyExistsException):
        user_service.register_user("testuser", "password")


def test_process_service_upload_fileobj_failure():
    user_repository = Mock()
    process_repository = Mock()
    publish_queue = Mock()
    storage_service = Mock()

    fileobj = Mock()
    file_name = "testfile.mp4"

    storage_service.upload_fileobj.side_effect = Exception("Upload failed")

    process_service = ProcessService(
        user_repository, process_repository, publish_queue, storage_service
    )

    with pytest.raises(Exception):
        process_service.upload_fileobj(fileobj, file_name)
