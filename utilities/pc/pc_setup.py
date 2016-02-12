import re
import subprocess

import requests

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

def write_to_bash_file(master_ips, my_ips, filename):
    with open(filename, "w") as bash_file:
        bash_file.write("export ROS_HOSTNAME={}\n".format(my_ips[0]))
        bash_file.write("export ROS_MASTER_URI={}\n".format(master_ips[0]))

if __name__ == "__main__":
    r = requests.get("http://thewrong.info/static/robot/ips.json")
    
    my_ips = find_public_ips()
    
    write_to_bash_file(r.json(), my_ips, "pc_ip.sh")
