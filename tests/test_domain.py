import pytest
from datetime import datetime
from enum import Enum
from dataclasses import asdict
from domain.entities import UserEntity, ProcessEntity, ProcessStatus


@pytest.fixture
def user_entity():
    return UserEntity(
        id=1,
        username="testuser",
        password="testpassword",
        created_at=datetime(2023, 10, 1, 12, 0, 0),
        updated_at=datetime(2023, 10, 2, 12, 0, 0),
    )


@pytest.fixture
def user_entity_no_updated_at():
    return UserEntity(
        id=1,
        username="testuser",
        password="testpassword",
        created_at=datetime(2023, 10, 1, 12, 0, 0),
    )


@pytest.fixture
def process_entity():
    return ProcessEntity(
        id="process-123",
        status=ProcessStatus.STARTED,
        name="Test Process",
        user_id=1,
        created_at=datetime(2023, 10, 1, 12, 0, 0),
        updated_at=datetime(2023, 10, 2, 12, 0, 0),
    )


@pytest.fixture
def process_entity_no_updated_at():
    return ProcessEntity(
        id="process-123",
        status=ProcessStatus.STARTED,
        name="Test Process",
        user_id=1,
        created_at=datetime(2023, 10, 1, 12, 0, 0),
    )


def test_user_entity_as_dict(user_entity):
    user_dict = user_entity.as_dict()

    expected_dict = {
        "id": 1,
        "username": "testuser",
        "password": "testpassword",
        "created_at": datetime(2023, 10, 1, 12, 0, 0),
        "updated_at": datetime(2023, 10, 2, 12, 0, 0),
    }

    assert user_dict == expected_dict


def test_user_entity_as_dict_no_updated_at(user_entity_no_updated_at):
    user_dict = user_entity_no_updated_at.as_dict()

    expected_dict = {
        "id": 1,
        "username": "testuser",
        "password": "testpassword",
        "created_at": datetime(2023, 10, 1, 12, 0, 0),
    }

    assert user_dict == expected_dict


def test_user_entity_from_dict():
    user_data = {
        "id": 1,
        "username": "testuser",
        "password": "testpassword",
        "created_at": datetime(2023, 10, 1, 12, 0, 0),
        "updated_at": datetime(2023, 10, 2, 12, 0, 0),
    }

    user_entity = UserEntity.from_dict(user_data)

    assert user_entity.id == 1
    assert user_entity.username == "testuser"
    assert user_entity.password == "testpassword"
    assert user_entity.created_at == datetime(2023, 10, 1, 12, 0, 0)
    assert user_entity.updated_at == datetime(2023, 10, 2, 12, 0, 0)


def test_process_entity_as_dict(process_entity):
    process_dict = process_entity.as_dict()

    expected_dict = {
        "id": "process-123",
        "status": ProcessStatus.STARTED.value,
        "name": "Test Process",
        "user_id": 1,
        "created_at": datetime(2023, 10, 1, 12, 0, 0),
        "updated_at": datetime(2023, 10, 2, 12, 0, 0),
    }

    assert process_dict == expected_dict


def test_process_entity_as_dict_no_updated_at(process_entity_no_updated_at):
    process_dict = process_entity_no_updated_at.as_dict()

    expected_dict = {
        "id": "process-123",
        "status": ProcessStatus.STARTED.value,
        "name": "Test Process",
        "user_id": 1,
        "created_at": datetime(2023, 10, 1, 12, 0, 0),
    }

    assert process_dict == expected_dict


def test_process_entity_from_dict():
    process_data = {
        "id": "process-123",
        "status": ProcessStatus.STARTED.value,
        "name": "Test Process",
        "user_id": 1,
        "created_at": datetime(2023, 10, 1, 12, 0, 0),
        "updated_at": datetime(2023, 10, 2, 12, 0, 0),
    }

    process_entity = ProcessEntity.from_dict(process_data)

    assert process_entity.id == "process-123"
    assert process_entity.status == ProcessStatus.STARTED
    assert process_entity.name == "Test Process"
    assert process_entity.user_id == 1
    assert process_entity.created_at == datetime(2023, 10, 1, 12, 0, 0)
    assert process_entity.updated_at == datetime(2023, 10, 2, 12, 0, 0)


def test_process_status_from_value():
    status = ProcessStatus.from_value(1)
    assert status == ProcessStatus.STARTED

    status = ProcessStatus.from_value(5)
    assert status == ProcessStatus.FINISHED


def test_process_status_invalid_value():
    with pytest.raises(ValueError):
        ProcessStatus.from_value(99)
