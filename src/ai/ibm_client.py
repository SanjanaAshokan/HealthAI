# src/ai/ibm_client.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WATSON_API_KEY")
API_URL = os.getenv("WATSON_API_URL")         # base URL from IBM Cloud
DEPLOYMENT_ID = os.getenv("WATSON_DEPLOYMENT_ID")

def call_granite(prompt: str, max_tokens: int = 512, temperature: float = 0.2):
    """
    Generic wrapper: POST to your IBM deployment endpoint with prompt and return model text.
    Replace the request URL and payload structure with the exact IBM required format.
    """
    if not API_KEY or not API_URL or not DEPLOYMENT_ID:
        raise ValueError("Missing IBM credentials. Set WATSON_API_KEY, WATSON_API_URL, WATSON_DEPLOYMENT_ID in .env")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "input": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature
        # Adjust keys according to IBM API contract
    }

    # Example target URL: you will replace this with IBM's actual endpoint for inference
    url = f"{API_URL}/deployments/{DEPLOYMENT_ID}/predictions"

    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    # Interpret the response — structure depends on IBM's API
    # Example: assume data['predictions'][0]['output_text'] or similar
    # Adjust accordingly to match real IBM response.
    try:
        # conservative extraction:
        text = (
            data.get("predictions", [{}])[0]
            .get("output_text")
            or data.get("result", {}).get("text")
            or str(data)
        )
    except Exception:
        text = str(data)

    return text
