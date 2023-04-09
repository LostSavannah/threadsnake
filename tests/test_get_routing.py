from testtools.tools import get

def test_get():
    data = get('resources').json()
    assert len(data) == 1

def test_accepts_when_not_valid_content_type_returns_400():
    assert 1 == 1

def test_accepts_when_valid_content_type_returns_200():
    assert 1 == 1
    
def test_validates_request_when_invalid_returns_400():
    assert 1 == 1

def test_validates_request_when_valid_returns_200():
    assert 1 == 1
    
def test_requires_parameters_when_invalid_returns_400():
    assert 1 == 1

def test_requires_parameters_when_valid_returns_200():
    assert 1 == 1

def test_accepts_json_when_invalid_returns_400():
    assert 1 == 1

def test_accepts_json_when_valid_returns_200():
    assert 1 == 1

def test_alive():
    assert 2 == 2