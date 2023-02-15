import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    print(f"Response is {r.text}")
    # print(f"response Body is {r.json()}")
    body = r.json()
    assert body['name'] == 'Chris Wanstrath'
    # print(f"Response Srtatus code is {r.status_code}")
    assert r.status_code == 200
    # print(f"Response Header are {r.headers}")
    headers = r.headers
    assert headers['Server'] == 'GitHub.com'

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')
    assert r.status_code == 404