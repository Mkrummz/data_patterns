import boto3
from botocore.exceptions import NoCredentialsError

# Credentials for authentication
access_key = 'your_access_key'
secret_key = 'your_secret_key'
bucket_name = 'internal-datalake'
file_path = 'data/batch-upload.csv'
object_key = 'batch-data/uploads/2024/batch-upload.csv'

# Initialize the S3 client using boto3 (can be a data lake SDK wrapper)
s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Upload large file in multiple parts
def multipart_upload(file_path, bucket, object_key):
    try:
        response = s3_client.upload_file(file_path, bucket, object_key)
        print(f"File {file_path} uploaded successfully as {object_key}.")
    except NoCredentialsError:
        print("Credentials not available.")

# Call the multi-part upload function
multipart_upload(file_path, bucket_name, object_key)
