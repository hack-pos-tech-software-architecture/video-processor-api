import boto3

from ports.storage_service import StorageServiceInterface

s3_client = boto3.client("s3", region_name="us-east-1")


class StorageS3(StorageServiceInterface):

    def __init__(self, bucket_name: str = "test-storage-videos"):
        self._bucket_name = bucket_name

    def upload_file(self, file_path: str, file_name: str) -> str:
        s3_client.upload_file(file_path, self._bucket_name, file_name)
        s3_url = f"https://{self._bucket_name}.s3.us-east-1.amazonaws.com/{file_name}"
        return s3_url
