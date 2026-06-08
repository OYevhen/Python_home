import ssh_utils
import pytest
import json
# import allure

host = "172.30.0.114"


def test_t107():
    result = ssh_utils.ssh_cmd(host, "docker exec -it nginx sh -c 'nginx -t'")
    text = (result.get("stdout"))

    assert "syntax is ok" in text
    assert "test is successful" in text
    assert result.get("exit_code") == 0


def test_t119():
    result = ssh_utils.ssh_cmd(host, "docker container ps -a --format '{{.Names}}'")
    text = (result.get("stdout"))

    assert "dcp-init-box" in text
    assert "nginx" in text
    assert "web" in text
    assert "zabbix-web-nginx" in text
    assert "zabbix-agent" in text
    assert "backend" in text
    assert "zabbix-server" in text
    assert "pgsql-server-zabbix" in text
    assert "pgsql-server-platform" in text
    assert "redis" in text
    assert result.get("exit_code") == 0


def save_cookie():
    json_data = '{"identifier":"user","password":"cmRzMTIzUkRTIQ==","rememberMe":false}'
    cmd = f"""curl -i -c cookies.txt 'http://{host}/api/v1/auth/sign-in' -H 'Content-Type: application/json' --data-raw '{json_data}' --insecure"""
    run_cmd = ssh_utils.ssh_cmd(host, cmd)
    print(run_cmd.get('stdout'))

save_cookie()


def test_sign_in():
    json_data = '{"identifier":"user","password":"cmRzMTIzUkRTIQ==","rememberMe":false}'
    cmd = f"""curl -i -s -b cookies.txt http://{host}/api/v1/auth/sign-in -H 'Content-Type: application/json' --data-raw '{json_data}' --insecure"""
    run_cmd = ssh_utils.ssh_cmd(host, cmd)
    
    stdout = run_cmd.get('stdout')
    exit_code = run_cmd.get('exit_code')
    
    assert "HTTP/1.1 200 OK" in stdout, "Expected 'HTTP/1.1 200 OK'"

@pytest.mark.sandbox
@pytest.mark.api
# @allure.title('Get storage pools')
def test_get_pools():
    """
    Verify that GET /api/v1/block-storage/pools returns block storage pools successfully.

    **Endpoint**::

        GET /api/v1/block-storage/pools

    **Command example**::

        curl -X 'GET' 'http://127.0.0.1/api/v1/block-storage/pools' -H 'accept: application/json'

    Setup:

        - None

    Test body:

        - Send GET request to /api/v1/block-storage/pools
        - Verify block storage pools response body

    Teardown:

        - None
    """
    # with allure.step('Send GET request to /api/v1/block-storage/pools'):
    cmd = f"curl -s -b cookies.txt http://{host}/api/v1/block-storage/pools -H 'accept: application/json'"
    run_cmd = ssh_utils.ssh_cmd(host, cmd)

    stdout = run_cmd.get('stdout')
    exit_code = run_cmd.get('exit_code')
    assert stdout

    data = json.loads(stdout)

    assert isinstance(data, list)
    assert len(data) == 2

    for pool in data:
        pool_id = pool.get('id')
        assert pool_id == 'sda1'
        pool_name = pool.get('name')
        assert pool_name == 'sda1'
        cluster_name = pool.get('clusterName')
        assert cluster_name == 'StarWind CVM'
    assert exit_code == 0
        
        # data = json.loads(stdout)
        # print(json.dumps(data, indent=3))
        
        # assert data[0].get('clusterName') == 'StarWind CVM', f"{data[0].get('clusterName')} != 'StarWind CVM'"
        # assert data[0].get('name') == 'sda1', f"{data[0].get('name')} != 'sda1'"
        # assert exit_code == 0, f"Exit code is {exit_code}, expected 0"    

