import pytest
from unittest.mock import Mock, patch
from adapters.orm.repositories import ProcessRepository, UserRepository
from domain.entities import UserEntity, ProcessEntity, ProcessStatus
from adapters.orm.models import UserModel, ProcessModel


def test_user_repository_create_user_success():
    user_model_mock = Mock()
    user_model_mock.model_to_dict.return_value = {
        "username": "testuser",
        "password": "hashedpassword",
    }

    with patch("adapters.orm.models.UserModel.create", return_value=user_model_mock):
        user_repository = UserRepository()
        user = user_repository.create_user(
            UserEntity(username="testuser", password="hashedpassword")
        )

        assert user.username == "testuser"
        assert user.password == "hashedpassword"


def test_user_repository_create_user_failure():
    with patch("adapters.orm.models.UserModel.create", return_value=None):
        user_repository = UserRepository()
        user = user_repository.create_user(
            UserEntity(username="testuser", password="hashedpassword")
        )

        assert user is None


def test_user_repository_get_by_username_success():
    user_model_mock = Mock()
    user_model_mock.model_to_dict.return_value = {
        "username": "testuser",
        "password": "hashedpassword",
    }

    with patch(
        "adapters.orm.models.UserModel.get_or_none", return_value=user_model_mock
    ):
        user_repository = UserRepository()
        user = user_repository.get_by_username("testuser")

        assert user.username == "testuser"
        assert user.password == "hashedpassword"


def test_user_repository_get_by_username_failure():
    with patch("adapters.orm.models.UserModel.get_or_none", return_value=None):
        user_repository = UserRepository()
        user = user_repository.get_by_username("testuser")

        assert user is None


def test_user_repository_get_by_id():
    user_repository = UserRepository()
    result = user_repository.get_by_id(1)

    assert result is True


def test_process_repository_create_success():
    process_model_mock = Mock()
    process_model_mock.model_to_dict.return_value = {
        "user_id": 1,
        "status": ProcessStatus.STARTED.value,
        "name": "Test Process",
    }

    with patch(
        "adapters.orm.models.ProcessModel.create", return_value=process_model_mock
    ):
        process_repository = ProcessRepository()
        process = process_repository.create(
            ProcessEntity(user_id=1, status=ProcessStatus.STARTED, name="Test Process")
        )

        assert process.user_id == 1
        assert process.status == 1
        assert process.name == "Test Process"


def test_process_repository_create_failure():
    with patch("adapters.orm.models.ProcessModel.create", return_value=None):
        process_repository = ProcessRepository()
        process = process_repository.create(
            ProcessEntity(user_id=1, status=ProcessStatus.STARTED, name="Test Process")
        )

        assert process is None
