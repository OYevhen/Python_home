import requests
from units import URL1, token1



def test_wizard_run():
    token = token1

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
            "hostname": f"CVM-{URL1.split('.')[-1]}"
        }
    }

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    response = requests.post(f"{URL1}/api/v1/wizard/run", json=payload, headers=headers, verify=False)

    print("STATUS:", response.status_code)
    print("BODY:", response.text)
