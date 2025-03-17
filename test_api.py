import requests

# Flask API URL (running locally)
API_URL = "http://127.0.0.1:5001/chat"

# Request Headers
HEADERS = {"Content-Type": "application/json"}

# Message to Send
DATA = {"message": "How can I use Flask with Mistral AI?"}

# Sending the API Request
try:
    response = requests.post(API_URL, json=DATA, headers=HEADERS)
    response_data = response.json()
    
    # Print the response
    print("Mistral AI Response:", response_data["choices"][0]["message"]["content"])

except requests.exceptions.RequestException as e:
    print("Error:", e)
