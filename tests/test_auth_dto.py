import pytest
from datetime import datetime
from domain.entities import UserEntity
from adapters.dto.auth_dto import OutputUserDTO


@pytest.fixture
def user_entity():
    return UserEntity(
        id=1,
        username="testuser",
        password="123",
        created_at=datetime(2023, 10, 1, 12, 0, 0),
        updated_at=datetime(2023, 10, 2, 12, 0, 0),
    )


@pytest.fixture
def user_entity_no_updated_at():
    return UserEntity(
        id=1,
        username="testuser",
        password="123",
        created_at=datetime(2023, 10, 1, 12, 0, 0),
        updated_at=None,
    )


def test_from_domain(user_entity):
    output_user_dto = OutputUserDTO.from_domain(user_entity)

    assert output_user_dto.id == user_entity.id
    assert output_user_dto.username == user_entity.username
    assert output_user_dto.created_at == "2023-10-01T12:00:00Z"
    assert output_user_dto.updated_at == "2023-10-02T12:00:00Z"


def test_from_domain_no_updated_at(user_entity_no_updated_at):
    output_user_dto = OutputUserDTO.from_domain(user_entity_no_updated_at)

    assert output_user_dto.id == user_entity_no_updated_at.id
    assert output_user_dto.username == user_entity_no_updated_at.username
    assert output_user_dto.created_at == "2023-10-01T12:00:00Z"
    assert output_user_dto.updated_at is None


def test_to_dict(user_entity):
    output_user_dto = OutputUserDTO.from_domain(user_entity)
    output_dict = output_user_dto.to_dict()

    expected_dict = {
        "id": user_entity.id,
        "username": user_entity.username,
        "created_at": "2023-10-01T12:00:00Z",
        "updated_at": "2023-10-02T12:00:00Z",
    }

    assert output_dict == expected_dict


def test_to_dict_no_updated_at(user_entity_no_updated_at):
    output_user_dto = OutputUserDTO.from_domain(user_entity_no_updated_at)
    output_dict = output_user_dto.to_dict()

    expected_dict = {
        "id": user_entity_no_updated_at.id,
        "username": user_entity_no_updated_at.username,
        "created_at": "2023-10-01T12:00:00Z",
    }

    assert output_dict == expected_dict
