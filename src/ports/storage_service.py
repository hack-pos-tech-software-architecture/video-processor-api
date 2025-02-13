from typing import BinaryIO, Optional, Dict, List
from abc import ABC, abstractmethod


class StorageServiceInterface(ABC):

    @abstractmethod
    def upload_fileobj(self, fileobj: BinaryIO, file_key: str) -> str:
        raise NotImplementedError
