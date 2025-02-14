from typing import Dict
from datetime import datetime
import uuid

from playhouse.shortcuts import model_to_dict
from peewee import (
    Model,
    CharField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    UUIDField,
)

from adapters.orm.config import get_database

db = get_database()


class BaseModel(Model):
    created_at: datetime = DateTimeField(default=datetime.now)
    updated_at: datetime = DateTimeField(null=True)

    def model_to_dict(self) -> Dict:
        return model_to_dict(self)

    class Meta:
        database = db


class UserModel(BaseModel):
    username: str = CharField(max_length=120)
    password: str = CharField()

    def model_to_dict(self) -> Dict:
        return model_to_dict(self)

    class Meta:
        table_name = "users"


class ProcessModel(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField()
    status = IntegerField()
    user_id = ForeignKeyField(UserModel, backref="processes")

    class Meta:
        table_name = "processes"


class SubprocessModel(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    status = IntegerField()
    process_id = ForeignKeyField(ProcessModel, backref="subprocesses")
    user_id = ForeignKeyField(UserModel)

    class Meta:
        table_name = "subprocesses"


class SubprocessItemModel(BaseModel):
    subprocess_id = ForeignKeyField(SubprocessModel, backref="subprocesses_items")
    user_id = ForeignKeyField(UserModel)
    image_url = CharField()

    class Meta:
        table_name = "subprocess_items"
