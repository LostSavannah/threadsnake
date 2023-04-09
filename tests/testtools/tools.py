import requests
from warnings import filterwarnings

filterwarnings('ignore', 'request is being made to')

base_url = 'http://localhost:9090'

def get(relative_url:str) -> requests.Response:
    return requests.get(f'{base_url}/{relative_url}', verify=False)