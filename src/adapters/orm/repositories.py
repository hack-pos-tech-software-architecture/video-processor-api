from adapters.orm.models import ProcessModel, UserModel
from domain.entities import ProcessEntity, UserEntity
from ports.repositories import ProcessRepositoryInterface, UserRepositoryInterface


class UserRepository(UserRepositoryInterface):

    def create_user(self, user: UserEntity) -> UserEntity | None:
        user = UserModel.create(username=user.username, password=user.password)
        if not user:
            return None
        return UserEntity(**user.model_to_dict())

    def get_by_username(self, username: str) -> UserEntity | None:
        user = UserModel.get_or_none(username=username)
        if not user:
            return None
        return UserEntity(**user.model_to_dict())

    def get_by_id(self, user_id: int) -> UserEntity | None:
        return True


class ProcessRepository(ProcessRepositoryInterface):

    def create(self, process: ProcessEntity) -> ProcessEntity | None:
        process = ProcessModel.create(
            user_id=process.user_id, status=process.status.value, name=process.name
        )
        if not process:
            return None
        return ProcessEntity(**process.model_to_dict())
