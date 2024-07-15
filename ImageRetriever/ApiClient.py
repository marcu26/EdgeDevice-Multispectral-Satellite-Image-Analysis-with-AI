import json
import requests
import urllib3

# Suppress only the self-signed certificate warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def send_to_api(api_url, payload):
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(payload), verify=False)

    print(response.text)
