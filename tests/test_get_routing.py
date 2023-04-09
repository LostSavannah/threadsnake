import requests
from warnings import filterwarnings

filterwarnings('ignore', 'request is being made to')

base_url = 'http://localhost:9090'

def test_get():
    data = requests.get(f'{base_url}/users', verify=False).text
    print(data)

def test_alive():
    assert 2 == 2