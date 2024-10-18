from onestream_sdk import OneStreamClientWrapper  # Hypothetical SDK wrapper for OneStream
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import time
import io

# Initialize OneStream client wrapper
client = OneStreamClientWrapper(api_key="your_onestream_api_key", endpoint="https://onestream.example.com")

# Sample data in pandas DataFrame
data = {
    'product_id': ['P001', 'P002', 'P003'],
    'price': [19.99, 29.99, 9.99],
    'stock': [100, 50, 200]
}

df = pd.DataFrame(data)

# Perform data validation (schema check)
expected_columns = ['product_id', 'price', 'stock']
if all(col in df.columns for col in expected_columns):
    print("Schema validation passed.")
else:
    print("Schema validation failed. Aborting upload.")
    exit(1)

# Convert DataFrame to an in-memory Parquet file (buffer)
parquet_buffer = io.BytesIO()  # Create an in-memory buffer
table = pa.Table.from_pandas(df)  # Convert Pandas DataFrame to PyArrow Table
pq.write_table(table, parquet_buffer)  # Write table to Parquet format in-memory

# Reset buffer pointer to the beginning
parquet_buffer.seek(0)

# Additional input parameters
team_tag = "BusinessAnalytics"
dataset_version = "v1.2"
upload_time = time.time()

# Upload the in-memory Parquet data to OneStream with additional metadata
response = client.upload_file(
    file_object=parquet_buffer,  # Pass the in-memory buffer as the file object
    destination_path='/parquet-datasets/2024/products',
    format='parquet',
    metadata={
        'team_tag': team_tag,
        'dataset_version': dataset_version,
        'upload_time': str(upload_time)
    }
)

# Check the response to ensure the upload was successful
if response.get("status") == "success":
    print("Parquet data successfully uploaded to OneStream.")
else:
    print(f"Upload failed: {response.get('error')}")
