import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error: pin_to_ipfs expects a dictionary"

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data)

    # Define the endpoint for pinning to IPFS
    ipfs_url = 'https://ipfs.infura.io:5001/api/v0/add'

    infura_project_id = '8e029658709540f6bc1fb9b8f0a270c8'
    infura_project_secret = '3V+HceQMSpSdLgVgLVIvc9TLb/hzrjDihlqA8XtpJOvrU4KGtmBdcw'
    # Headers for basic authentication
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f"{infura_project_id}:{infura_project_secret}".encode()).decode()
    }

    # Send a POST request with the JSON data
    response = requests.post(ipfs_url, headers=headers, files={"file": json_data})
    response.raise_for_status()  # This will raise an error for a failed request

    # Extract the CID from the response
    cid = response.json()["Hash"]

    return cid

def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), "get_from_ipfs accepts a cid in the form of a string"

    # Define the endpoint for retrieving from IPFS
    ipfs_gateway_url = f'https://ipfs.infura.io/ipfs/{cid}'

    # Send a GET request
    response = requests.get(ipfs_gateway_url)
    response.raise_for_status()

    # Assuming the content is JSON, parse it into a Python dictionary
    data = response.json()

    assert isinstance(data, dict), "get_from_ipfs should return a dict"

    return data
