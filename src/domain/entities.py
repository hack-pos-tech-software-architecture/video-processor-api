from enum import Enum
from datetime import datetime
from typing import Dict
from dataclasses import dataclass, asdict, field


class ProcessStatus(Enum):
    STARTED = 1
    PROCESSING = 2
    ABORTED = 3
    FAILED = 4
    FINISHED = 5

    @classmethod
    def from_value(cls, value):
        return cls(value=value)


@dataclass
class UserEntity:
    id: int = field(default=None, repr=False, kw_only=True)
    username: str
    password: str
    created_at: datetime = field(default=datetime.now(), kw_only=True)
    updated_at: datetime = field(default=None, kw_only=True)

    def as_dict(self) -> Dict:
        serialized = asdict(
            self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None}
        )
        return serialized

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(**data)


@dataclass
class ProcessEntity:
    id: str = field(default=None, repr=False, kw_only=True)
    status: ProcessStatus
    name: str
    user_id: int
    created_at: datetime = field(default=datetime.now(), kw_only=True)
    updated_at: datetime = field(default=None, kw_only=True)

    def as_dict(self) -> Dict:
        serialized = asdict(
            self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None}
        )
        serialized["status"] = self.status.value
        return serialized

    @classmethod
    def from_dict(cls, data: Dict):
        data_copy = data
        data_copy["status"] = ProcessStatus(data["status"])
        return cls(**data)
