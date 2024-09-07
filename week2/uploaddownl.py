import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_file(path, bucket, object_name):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename("picture.png")

    # Upload the file
    s3_client = boto3.client(
    's3',
    aws_access_key_id=,
    aws_secret_access_key=
    )
    try:
        response = s3_client.upload_file("C:\\Users\\ArbinM\\Pictures\\picture.png", bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
def download_file(bucket, object, path):
    s3 = boto3.client(
    's3',
    aws_access_key_id=,
    aws_secret_access_key=
    )
    s3.download_file(bucket, object, path)
