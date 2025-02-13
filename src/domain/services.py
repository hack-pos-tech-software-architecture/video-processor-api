from datetime import datetime
import os
from concurrent.futures import ThreadPoolExecutor
import time

from domain.entities import ProcessEntity, ProcessStatus, UserEntity

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
            token = self._access_token.generate_token(payload=user.username)
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
        # publish_queue: PublishQueueInterface,
        storage_service: StorageServiceInterface,
    ):
        self._user_repository = user_repository
        self._process_repository = process_repository
        # self._publish_queue = publish_queue
        self._storage_service = storage_service

    def thread_upload_multiple_files(
        self, filepath: str, filename: str, processId: str
    ):
        start_time = datetime.now()
        print(f"[{start_time}] Iniciando upload do arquivo: {filename}")
        storage_url = self._storage_service.upload_file(
            file_path=filepath, file_name=filename
        )
        self.processed_files.append(
            {
                "process_id": processId,
                "file_name": filename,
                "file_url": storage_url,
            }
        )
        os.remove(filepath)
        end_time = datetime.now()
        print(f"[{end_time}] Upload concluído para: {filename}")

    def upload_multiple_files(self, files: list, user_id: int) -> bool:

        user = self._user_repository.get_by_id(user_id=user_id)
        if not user:
            raise Exception("Usuário não encontrado.")

        errors = []

        start_time = time.time()
        with ThreadPoolExecutor(max_workers=5) as executor:
            for file in files:
                if file.filename == "":
                    errors.append({"file": "Unnamed file in request"})
                    continue

                filename = file.filename
                filepath = os.path.join("uploads", filename)
                file.save(filepath)

                process = self._process_repository.create(
                    ProcessEntity(
                        status=ProcessStatus.STARTED, user_id=user_id, name=filename
                    )
                )

                # self.thread_upload_multiple_files(filepath, filename, process.id)

                executor.submit(
                    self.thread_upload_multiple_files, filepath, filename, process.id
                )

                # message = {
                #     "process_id": process.id,
                #     "file_name": filename,
                #     "file_url": "storage_url",
                # }

                # self._publish_queue.publish(message=message)

                # uploaded_files.append(message)
            # print(f"############### --> {self.processed_files}")
        end_time = time.time()
        print(f"Tempo total: {end_time - start_time:.2f} segundos")