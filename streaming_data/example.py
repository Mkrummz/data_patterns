import websocket
import json
import time

# Authentication token for the WebSocket
auth_token = "Bearer your_auth_token"

# WebSocket URL of the internal data lake stream endpoint
ws_url = "wss://datalake.example.com/streaming"

# Sample streaming data
stream_data = {
    "sensor_id": "ABC123",
    "temperature": 22.5,
    "timestamp": time.time(),
    "status": "active"
}

# WebSocket connection and sending data to the lake
def on_open(ws):
    print("Connection opened.")
    ws.send(json.dumps(stream_data))

def on_message(ws, message):
    print("Message received from the data lake:", message)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws):
    print("Connection closed.")

# Add auth token to WebSocket header
headers = [
    f"Authorization: {auth_token}"
]

ws = websocket.WebSocketApp(ws_url,
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close,
                            header=headers)

# Connect and stream data
ws.run_forever()
