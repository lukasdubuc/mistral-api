import requests

API_KEY = "DyuEyWPGj6KEkebcSxiYhjtV4SgSrG20"
url = "https://api.mistral.ai/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

data = {
    "model": "open-mistral-7b",
    "messages": [{"role": "user", "content": "Hello, Mistral!"}]
}

try:
    response = requests.post(url, json=data, headers=headers, timeout=10)  # Set timeout
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
