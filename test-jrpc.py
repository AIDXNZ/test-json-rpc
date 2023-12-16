import requests
import json

def test_json_rpc(url, method, params):
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 2,
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers).json()

    return response

# Usage
token = "mytoken"
url = "http://127.0.0.1:1234/rpc/v0?token=" + token
method = "Filecoin.ClientDealPieceCID"
params = [{
"/": "bafy2bzacea3wsdh6y3a36tb3skempjoxqpuyompjbmfeyf34fi3uy6uue42sdsdsdsdsds"
}]
print(test_json_rpc(url, method, params))
