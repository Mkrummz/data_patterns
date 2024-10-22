import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import time

# Credentials and settings for DataLake (could be similar to S3)
access_key = 'your_datalake_access_key'
secret_key = 'your_datalake_secret_key'
region = 'us-west-2'
bucket_name = 'datalake-datalake'
file_path = 'data/multi-part-upload.csv'
object_key = 'datasets/2024/multi-part-upload.csv'

# Additional metadata
team_tag = "DataOps"
batch_id = "batch_2024_01"
upload_timestamp = time.time()

# Initialize DataLake client (AWS S3 compatible)
s3_client = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Upload large file in multiple parts
def multipart_upload(file_path, bucket, object_key, metadata):
    try:
        s3_client.upload_file(file_path, bucket, object_key, ExtraArgs={'Metadata': metadata, 'StorageClass': 'STANDARD_IA'})
        print(f"File {file_path} successfully uploaded to {object_key}.")
    except (NoCredentialsError, ClientError) as e:
        print(f"Failed to upload file: {str(e)}")

# Call multi-part upload
metadata = {
    'team_tag': team_tag,
    'batch_id': batch_id,
    'upload_timestamp': str(upload_timestamp)
}
multipart_upload(file_path, bucket_name, object_key, metadata)
