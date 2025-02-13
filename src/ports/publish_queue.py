from abc import ABC, abstractmethod


class PublishQueueInterface(ABC):

    @abstractmethod
    def publish(self, message: dict) -> bool:
        raise NotImplementedError
