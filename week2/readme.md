# WEEK 2 : Working with Buckets and AWS S3 SDK

### TASK 1: Creating a Bucket:
1. Logging into IAM Account
2. Creating access keys     
![creating keys](0.png)
4. Changing Server to asia-mumbai. (closest)
5. creating a bucket with unique name       
![1](1.png)   

4. Uploading [this](https://images.ctfassets.net/hrltx12pl8hq/4f6DfV5DbqaQUSw0uo0mWi/6fbcf889bdef65c5b92ffee86b13fc44/shutterstock_376532611.jpg?fit=fill&w=600&h=400) image to bucket using python SDK code.    

 ```
import logging
import boto3
from botocore.exceptions import ClientError
import os
def upload_file(path, bucket, object_name=None):
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = os.path.basename(file_name)
        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
```
![code-idle](3.png)      
![uploaded](4.png)

5. Downloading the image from the bucket using this code        
```
def download_file(bucket, object, path):
    s3 = boto3.client('s3')
    s3.download_file(bucket, object, path)
```      
![code](5.png)     
![downloaded](6.png)    

