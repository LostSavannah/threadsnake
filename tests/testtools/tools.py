from typing import Dict
import requests
from warnings import filterwarnings

filterwarnings('ignore', 'request is being made to')

base_url = 'http://localhost:9090'

def get(relative_url:str, headers:Dict[str, str] = None) -> requests.Response:
    headers = headers or {}
    return requests.get(f'{base_url}/{relative_url}', verify=False, headers=headers)


