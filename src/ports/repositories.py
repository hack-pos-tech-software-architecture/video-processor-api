from abc import ABC, abstractmethod

from domain.entities import ProcessEntity, UserEntity


class UserRepositoryInterface(ABC):

    @abstractmethod
    def create_user(self, user: UserEntity) -> UserEntity | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_username(self, username: str) -> UserEntity | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: int) -> UserEntity | None:
        raise NotImplementedError


class ProcessRepositoryInterface(ABC):

    @abstractmethod
    def create(self, process: ProcessEntity) -> ProcessEntity | None:
        raise NotImplementedError
