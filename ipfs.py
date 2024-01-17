import requests
import json
import io

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error: pin_to_ipfs expects a dictionary"

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data)
    my_file = json_data + '.json'

    # Convert JSON string to a bytes stream
    json_bytes = io.BytesIO(json_data.encode())

    # Define the endpoint for pinning to IPFS
    ipfs_url = 'https://ipfs.infura.io:5001/api/v0/add'

    project_id = '8e029658709540f6bc1fb9b8f0a270c8'
    project_secret = '3V+HceQMSpSdLgVgLVIvc9TLb/hzrjDihlqA8XtpJOvrU4KGtmBdcw'

    files = {
        'file': (my_file, json_bytes)  # Use a tuple (filename, fileobj)
    }

    # Send a POST request with the JSON data
    response = requests.post(ipfs_url, files=files, auth=(project_id,project_secret))
    print(response.text)
    response.raise_for_status()  # This will raise an error for a failed request

    # Extract the CID from the response
    cid = response.json()["Hash"]
    print(cid)

    return cid


def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), "get_from_ipfs accepts a cid in the form of a string"

    params = (
        ('arg',cid),
    )

    # Define the endpoint for pinning to IPFS
    ipfs_url = 'https://ipfs.infura.io:5001/api/v0/cat'
    
    project_id = '8e029658709540f6bc1fb9b8f0a270c8'
    project_secret = '3V+HceQMSpSdLgVgLVIvc9TLb/hzrjDihlqA8XtpJOvrU4KGtmBdcw'

    response = requests.post(ipfs_url, params=params, auth=(project_id,project_secret))
    print(response)

    response.raise_for_status()

    # Assuming the content is JSON, parse it into a Python dictionary
    data = response.json()

    assert isinstance(data, dict), "get_from_ipfs should return a dict"

    return data
