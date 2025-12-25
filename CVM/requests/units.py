import requests

URL1 = 'https://172.16.6.145'


def test_login(url):
    payload = {
        "userName": "user",
        "password": "cmRzMTIzUkRT",
        "autologin": "false"
    }
    response = requests.post(f'{url}/api/v2/account/login', json=payload, verify=False)
    print("LOGIN STATUS:", response.status_code)
    print("LOGIN HEADERS:", response.headers)
    print("LOGIN BODY:", response.text)
    data = response.json()
    token = data['accessToken']
    print('accessToken: ', token)
    return token

token1 = test_login(URL1)

def node_id1():
    response = requests.get(f'{URL1}/api/v1')
    data = response.json()
    nodeid = data["Id"]
    return nodeid