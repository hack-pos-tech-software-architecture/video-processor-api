from datetime import datetime

from typing import BinaryIO
import uuid

from domain.entities import UserEntity

from domain.exceptions import NotAuthorizedException, UserAlreadyExistsException
from ports.access_token import AccessTokenInterface
from ports.publish_queue import PublishQueueInterface
from ports.repositories import ProcessRepositoryInterface, UserRepositoryInterface
from ports.password_hash import PasswordHashInterface
from ports.storage_service import StorageServiceInterface


class AuthService:

    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        password_hash: PasswordHashInterface,
        access_token: AccessTokenInterface,
    ):
        self._user_repository = user_repository
        self._password_hash = password_hash
        self._access_token = access_token

    def login(self, username, password) -> str | Exception:
        user = self._user_repository.get_by_username(username)
        if user and self._password_hash.compare_password(password, user.password):
            payload = {"username": user.username}
            token = self._access_token.generate_token(payload)
            return token
        raise NotAuthorizedException("Not Authorized.")


class UserService:

    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        password_hash: PasswordHashInterface,
    ):
        self._user_repository = user_repository
        self._password_hash = password_hash

    def register_user(self, username: str, password: str) -> UserEntity | None:
        user = self._user_repository.get_by_username(username)
        if user:
            raise UserAlreadyExistsException()
        hash_password = self._password_hash.hash_password(password)
        user = self._user_repository.create_user(UserEntity(username, hash_password))
        return user


class ProcessService:

    processed_files = []

    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        process_repository: ProcessRepositoryInterface,
        publish_queue: PublishQueueInterface,
        storage_service: StorageServiceInterface,
    ):
        self._user_repository = user_repository
        self._process_repository = process_repository
        self._publish_queue = publish_queue
        self._storage_service = storage_service

    def upload_fileobj(self, fileobj: BinaryIO, file_name: str) -> dict:
        try:
            file_id = str(uuid.uuid4())
            file_key = f"videos/{file_id}-{file_name}"

            self._storage_service.upload_fileobj(fileobj, file_key)

            message = {"file_key": file_key, "file_id": file_id}
            self._publish_queue.publish(message)

            return {
                "message": "Upload bem-sucedido",
                "file_key": file_key,
                "file_id": file_id,
            }
        except Exception as err:
            raise err
