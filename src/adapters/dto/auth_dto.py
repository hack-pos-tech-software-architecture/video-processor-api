from typing import Optional
from pydantic import BaseModel

from domain.entities import UserEntity


class OutputUserDTO(BaseModel):
    id: int
    username: str
    created_at: str
    updated_at: Optional[str] = None

    @classmethod
    def from_domain(cls, user: UserEntity):
        return cls(
            id=user.id,
            username=user.username,
            created_at=user.created_at.strftime(format="%Y-%m-%dT%H:%M:%SZ"),
            updated_at=(
                user.updated_at.strftime(format="%Y-%m-%dT%H:%M:%SZ")
                if user.updated_at
                else None
            ),
        )

    def to_dict(self):
        return self.model_dump(exclude_none=True)
