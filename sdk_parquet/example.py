from data_lake_sdk import DataLakeClient  # Hypothetical SDK wrapper
import pyarrow.parquet as pq
import pandas as pd

# Initialize the DataLake client with auth credentials
datalake_client = DataLakeClient(api_key="your_api_key", endpoint="https://datalake.example.com")

# Sample data in a pandas DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Write DataFrame to Parquet format
parquet_file = 'data/upload-file.parquet'
df.to_parquet(parquet_file, engine='pyarrow')

# Upload Parquet file to Data Lake using the SDK wrapper
datalake_client.upload_file(file_path=parquet_file, destination_path='/datasets/2024/people_data', format='parquet')

print("Parquet data successfully uploaded.")
