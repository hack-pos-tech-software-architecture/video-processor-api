from abc import ABC, abstractmethod


class PublishQueueInterface(ABC):

    @abstractmethod
    def publish(self, message: any) -> bool:
        raise NotImplementedError
