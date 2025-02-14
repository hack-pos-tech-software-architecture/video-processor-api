import boto3
import json

from ports.publish_queue import PublishQueueInterface

sqs_client = boto3.client("sqs", region_name="us-east-1")


class PublishQueueSQS(PublishQueueInterface):

    def __init__(self, queue_url: str):
        self._queue_url = queue_url

    def publish(self, message: dict) -> None:

        file_id = message["file_id"]
        file_key = message["file_key"]

        sqs_client.send_message(
            QueueUrl=self._queue_url,
            MessageBody=json.dumps(message),
            MessageGroupId=f"{file_id}:{file_key}",
            MessageDeduplicationId=file_id,
        )
