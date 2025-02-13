from abc import ABC, abstractmethod


class PasswordHashInterface(ABC):

    @abstractmethod
    def hash_password(self, password: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def compare_password(self, password: str, hash_password: str) -> bool:
        raise NotImplementedError
