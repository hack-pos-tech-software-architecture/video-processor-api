from abc import ABC, abstractmethod


class AccessTokenInterface(ABC):

    @abstractmethod
    def generate_token(self, payload: any) -> str:
        raise NotImplementedError

    @abstractmethod
    def refresh_token(self, payload: any) -> str:
        raise NotImplementedError
