# data_patterns

## Streaming Data to DataLake (WebSocket):
- wss://datalake.example.com/streaming
- Streams JSON data in real-time via WebSocket with Bearer Token authentication.

## Multi-part Upload to DataLake (Batch):
- https://datalake.example.com/upload/multipart
- Supports multi-part uploads for large files with metadata via API Key/Secret Key.

## Parquet File Upload to DataLake (SDK Wrapper):
- https://datalake.example.com/upload/file
- Uploads Parquet files with additional metadata, authenticated via API Key.




Modified OpenAPI 3.0 Spec for Either File Upload or In-Memory Parquet Data Upload