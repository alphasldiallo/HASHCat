import json

import requests

from exceptions import *

def api_request(path, base_url="https://lea.kz"):
    try:
        response = requests.get(base_url + path)
        if response.status_code == 404:
            raise LeakzNotLeaked
        return response.json()
    except requests.exceptions.RequestException:
        raise LeakzRequestException
    except json.decoder.JSONDecodeError as error:
        raise LeakzJSONDecodeException



def ONCH(hash):
    return api_request("/api/hash/" + hash).get("password")

