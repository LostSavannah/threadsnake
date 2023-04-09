import base64
from typing import Dict

Headers = Dict[str, str]

def bearer(token:str, headers:Headers = None) -> Headers:
    headers = headers or {}
    headers.update({
        "Authorization": f"Bearer {token}"
    })
    return headers

def basic_auth(user:str, password:str, headers:Headers = None) -> Headers:
    encoded = base64.b64encode(f'{user}:{password}'.encode()).decode()
    headers = headers or {}
    headers.update({
        "Authorization": f"Basic {encoded}"
    })
    return headers
    