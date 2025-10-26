import requests
import json
from flask import jsonify

# The URL for the public ISS location API
ISS_API_URL = "http://api.open-notify.org/iss-now.json"

# NOTE: The entry point now expects a standard Flask request object
def get_iss_position(request):
    """
    HTTP Cloud Function that proxies the ISS position.
    
    This function is the entry point, and the runtime handles starting 
    the web server (on port 8080) and routing the request to this function.

    Args:
        request (flask.Request): The request object.
    Returns:
        A Flask Response object (JSON data, status code, and headers).
    """
    try:
        # 1. Fetch the data from the external API
        response = requests.get(ISS_API_URL, timeout=10)
        # 2. Check for HTTP errors (like 4xx or 5xx)
        response.raise_for_status() 

        # 3. Parse the JSON response
        iss_data = response.json()
        
        # 4. Set CORS headers and return the response
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*' 
        }

        # Return a standard Flask-compatible tuple: (body, status_code, headers)
        return jsonify(iss_data), 200, headers

    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching ISS data: {e}"
        print(f"ERROR: {error_message}")
        return jsonify({"message": "error", "details": error_message}), 503, {'Content-Type': 'application/json'}

    except json.JSONDecodeError:
        error_message = "External API returned invalid JSON."
        print(f"ERROR: {error_message}")
        return jsonify({"message": "error", "details": error_message}), 502, {'Content-Type': 'application/json'}