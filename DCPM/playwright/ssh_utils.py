import paramiko

def ssh_cmd(host, command, username="user", password="rds123RDS", key_path=None, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=username, password=password, key_filename=key_path)

    _, stdout, stderr = client.exec_command(command, get_pty=True)
    result = {
        "stdout": stdout.read().decode(),
        # "stderr": stderr.read().decode(),
        "exit_code": stdout.channel.recv_exit_status(),
    }

    client.close()
    return result

def cmd(host, command):
    result = ssh_cmd(host, command)
    print(f"Command: {command}\n")
    print(f"{result['stdout']}")
    # print(f"STDERR: {result['stderr']}")
    print(f"Exit Code: {result['exit_code']}")


    
    
    
    
    
    
    # cmd = "curl -v -b cookies.txt http://127.0.0.1/api/v1/block-storage/pools -H 'accept: application/json' | jq"


    # cmd = """curl -i -c cookies.txt  'http://127.0.0.1/api/v1/auth/sign-in' -H 'Content-Type: application/json' --data-raw '{"identifier":"user","password":"cmRzMTIzUkRTIQ==","rememberMe":false}' --insecure"""
    # cmd = "curl -v -b cookies.txt http://127.0.0.1/api/v1/block-storage/pools -H 'accept: application/json' | jq"
    
    