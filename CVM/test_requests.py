import requests

URL = 'https://172.25.176.114'

def test_login():
    payload = {
        "userName": "user",
        "password": "cmRzMTIzUkRT",
        "autologin": "false"
    }
    response = requests.post(f'{URL}/api/v2/account/login', json=payload, verify=False)
    print("LOGIN STATUS:", response.status_code)
    print("LOGIN HEADERS:", response.headers)
    print("LOGIN BODY:", response.text)
    data = response.json()
    token = data['accessToken']
    print('accessToken: ', token)
    return token


def test_run():
    token = test_login()

    payload = {
        "nodeId": "0A669310-D52E-11F0-87FB-5542EDB26A56",
        "administrationLoginOptions": {
            "userName": "user",
            "newPassword": "cmRzMTIzUkRTIUAj",
            "fullName": "",
            "email": ""
        },
        "timeZoneOptions": {
            "timeZone": "Europe/Kyiv",
            "timeSyncMode": "host",
            "ntpServersIp": []
        },
        "hostNetworkOptions": {
            "hostname": f"CVM-{URL.split('.')[-1]}"
        }
    }

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    response = requests.post(f"{URL}/api/v1/wizard/run", json=payload, headers=headers, verify=False)

    print("STATUS:", response.status_code)
    print("BODY:", response.text)
