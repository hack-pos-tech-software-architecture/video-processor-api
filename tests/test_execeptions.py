import pytest

from domain.exceptions import (
    EntityAlreadyExistsException,
    EntityNotFoundException,
    NotAuthorizedException,
    UserAlreadyExistsException,
    UserNotFoundException,
)


def test_user_already_exists_exception():
    exception = UserAlreadyExistsException()
    assert str(exception) == "User already exists."
    assert exception.message == "User already exists."

    custom_message = "Custom user already exists message."
    exception = UserAlreadyExistsException(custom_message)
    assert str(exception) == custom_message
    assert exception.message == custom_message


def test_user_not_found_exception():
    exception = UserNotFoundException()
    assert str(exception) == "User not found."
    assert exception.message == "User not found."

    custom_message = "Custom user not found message."
    exception = UserNotFoundException(custom_message)
    assert str(exception) == custom_message
    assert exception.message == custom_message


def test_entity_not_found_exception():
    custom_message = "Entity not found."
    exception = EntityNotFoundException(custom_message)
    assert str(exception) == custom_message
    assert exception.message == custom_message


def test_entity_already_exists_exception():
    custom_message = "Entity already exists."
    exception = EntityAlreadyExistsException(custom_message)
    assert str(exception) == custom_message
    assert exception.message == custom_message


def test_not_authorized_exception():
    custom_message = "Not authorized."
    exception = NotAuthorizedException(custom_message)
    assert str(exception) == custom_message
    assert exception.message == custom_message
