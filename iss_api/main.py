import requests
import json
from flask import jsonify

# The URL for the public ISS location API
ISS_API_URL = "http://api.open-notify.org/iss-now.json"

def get_iss_position(request):
    """
    HTTP Cloud Function that proxies the ISS position from the Open Notify API.
    Args:
        request (flask.Request): The request object.
    Returns:
        The JSON response from the ISS API, or an error.
    """
    try:
        # Fetch the data from the external API
        response = requests.get(ISS_API_URL, timeout=10)
        response.raise_for_status() # Raise an exception for bad status codes

        # Parse and return the external API's JSON response
        iss_data = response.json()
        
        # Optionally, you can add CORS headers for web usage
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*' # Allows all domains to call your API
        }

        return (jsonify(iss_data), 200, headers)

    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, etc.
        error_message = f"Error fetching ISS data: {e}"
        print(f"ERROR: {error_message}")
        return jsonify({"message": "error", "details": error_message}), 500

    except json.JSONDecodeError:
        # Handle cases where the external API returns non-JSON data
        return jsonify({"message": "error", "details": "External API returned invalid JSON"}), 502