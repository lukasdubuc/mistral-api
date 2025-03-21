import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔹 Load Mistral API Key from environment variables
API_KEY = os.getenv("MISTRAL_API_KEY", "YOUR_DEFAULT_KEY")  # Replace with a real key or set in Render

# 🔹 API Endpoint and Headers
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

@app.route('/')
def home():
    """Health check route"""
    return "Mistral API is live!"

@app.route('/chat', methods=['POST'])
def chat():
    """Handles chat requests and forwards them to Mistral AI."""
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    mistral_data = {
        "model": "open-mistral-7b",
        "messages": [{"role": "user", "content": user_message}]
    }

    try:
        response = requests.post(MISTRAL_API_URL, json=mistral_data, headers=HEADERS)
        response_data = response.json()

        if response.status_code != 200:
            return jsonify({"error": "Mistral API request failed", "details": response_data}), response.status_code

        return jsonify(response_data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Request failed", "details": str(e)}), 500

# 🔹 Use Render's dynamic port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 for Render
    app.run(host="0.0.0.0", port=port)
