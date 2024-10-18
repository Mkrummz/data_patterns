# data_patterns

## Streaming Data to OneStream (WebSocket):
- wss://onestream.example.com/streaming
- Streams JSON data in real-time via WebSocket with Bearer Token authentication.

## Multi-part Upload to OneStream (Batch):
- https://onestream.example.com/upload/multipart
- Supports multi-part uploads for large files with metadata via API Key/Secret Key.

## Parquet File Upload to OneStream (SDK Wrapper):
- https://onestream.example.com/upload/file
- Uploads Parquet files with additional metadata, authenticated via API Key.




Modified OpenAPI 3.0 Spec for Either File Upload or In-Memory Parquet Data Upload



Based on the OpenAPI specification you provided, the API appears to only support file uploads via the application/octet-stream format, which is typically used for binary file uploads, such as Parquet files. The application/octet-stream media type in the request body is designed for handling binary data (i.e., files), not in-memory objects or streams.

