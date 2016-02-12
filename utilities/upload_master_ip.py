import re
import json
import subprocess

import pexpect


ip_pattern = "(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"

def find_public_ips():
    args = ["ifconfig", "-a"]
    output = subprocess.check_output(args)

    ip_addresses = []
    for line in output.splitlines():
        if 'inet addr' in line:
            ip_addresses.append(re.search(ip_pattern, line).group(0))

    ip_addresses.remove("127.0.0.1")
    
    return ip_addresses
    
def write_ips_to_file(ips, filename):
    with open(filename, "w") as ip_file:
        json.dump(ips, ip_file)
        
def send_to_server(ip_filename, config_filename):
    with open(config_filename) as config_file:
        config = json.load(config_file)
        
    batch = config["batch"]
    user = config["user"]
    host = config["host"]
    command = "sftp {}@{}".format(user, host)
    
    child = pexpect.spawn(command)
    child.expect('password:')
    child.sendline(config['password'])
    
    with open(config["batch"]) as batch_file:
        for line in batch_file:
            child.expect("sftp> ")
            child.sendline(line)

if __name__ == "__main__":
    ips = find_public_ips()
    write_ips_to_file(ips, "ips.json")
    send_to_server("ips.json", "server.cfg.json")
