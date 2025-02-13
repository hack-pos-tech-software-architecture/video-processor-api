from typing import Optional, Dict, List
from abc import ABC, abstractmethod


class StorageServiceInterface(ABC):

    @abstractmethod
    def upload_file(self, file_path: str, file_name: str) -> str:
        raise NotImplementedError
