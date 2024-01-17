import requests
import json
import io

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error: pin_to_ipfs expects a dictionary"

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data)

    # Define the endpoint for pinning to IPFS via Pinata
    pinata_endpoint = 'https://api.pinata.cloud/pinning/pinJSONToIPFS'

    pinata_api_key = 'f865ea47c1a5d6bb5be4'
    pinata_secret_api_key = '0249fa18398161acfedba66eb9c547b88c2206713ca128c8630af170cb909770'
    
    headers = {
        'pinata_api_key': pinata_api_key,
        'pinata_secret_api_key': pinata_secret_api_key
    }

    # Send a POST request with the JSON data
    response = requests.post(pinata_endpoint, headers=headers, json={"pinataContent": data})
    response.raise_for_status()  # Raise an error for a failed request

    # Extract the CID from the response
    cid = response.json()["IpfsHash"]
    print(cid)

    return cid


def get_from_ipfs(cid):
    assert isinstance(cid, str), "get_from_ipfs accepts a cid in the form of a string"

    # Define the endpoint for retrieving from IPFS via a public gateway
    ipfs_gateway_url = f'https://gateway.pinata.cloud/ipfs/{cid}'

    # Send a GET request
    response = requests.get(ipfs_gateway_url)
    response.raise_for_status()

    # Assuming the content is JSON, parse it into a Python dictionary
    data = response.json()

    assert isinstance(data, dict), "get_from_ipfs should return a dict"

    return data
