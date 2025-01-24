import json
import requests
from typing import Dict, Any

class APIClient:
    def __init__(self, config_path: str = "config.json"):
        self.config = self._load_config(config_path)
        
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from JSON file."""
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def send_request(self, data: Dict[str, Any]) -> requests.Response:
        """Send data to the configured endpoint with specified headers."""
        endpoint = self.config['api']['endpoint']
        headers = self.config['api']['headers']
        timeout = self.config['timeout']
        
        response = requests.post(
            url=endpoint,
            headers=headers,
            json=data,
            timeout=timeout
        )
        response.raise_for_status()
        return response

def main():
    # Example usage
    client = APIClient()
    
    # Example data to send
    data = {
        "message": "Hello, API!",
        "timestamp": "2025-01-23T22:52:01-06:00"
    }
    
    try:
        response = client.send_request(data)
        print(f"Success! Response status: {response.status_code}")
        print(f"Response data: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing response: {e}")

if __name__ == "__main__":
    main()
