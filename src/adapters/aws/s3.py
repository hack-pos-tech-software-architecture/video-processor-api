from typing import BinaryIO
import boto3

from ports.storage_service import StorageServiceInterface

s3_client = boto3.client("s3", region_name="us-east-1")


class StorageS3(StorageServiceInterface):

    def __init__(self, bucket_name: str):
        self._bucket_name = bucket_name

    def upload_fileobj(self, fileobj: BinaryIO, file_key: str) -> None:
        s3_client.upload_fileobj(fileobj, self._bucket_name, file_key)
