import os

from peewee import PostgresqlDatabase


def get_database():
    db = PostgresqlDatabase(
        database=os.environ.get("DATABASE_NAME"),
        host=os.environ.get("DATABASE_HOST"),
        port=os.environ.get("DATABASE_PORT"),
        user=os.environ.get("DATABASE_USER"),
        password=os.environ.get("DATABASE_PASSWORD"),
    )
    return db
