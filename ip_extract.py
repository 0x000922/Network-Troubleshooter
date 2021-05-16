import os
import re
import ipaddress


def extract_ip():
    list_files = os.listdir()
    f_name = ''
    if 'res.tcp' in list_files:
        f_name = 'res.tcp'
    elif 'res.icmp' in list_files:
        f_name = 'res.icmp'
    elif 'res.udp' in list_files:
        f_name = 'res.udp'
    else:
        print("file not found")

    with open(f_name) as fh:
        fstring = fh.readlines()

#    print(type(fstring))
    ips = []
    found = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', str(fstring))
    ips.extend(found)
#    test = re.findall(r'\\* \\* \\*', str(fstring))
#    l_ip_valid = []
    l_ip_valid_a = []
    l_ip_valid_set = set()
    for i in ips:
        try:
            if i not in l_ip_valid_set:
                l_ip_valid_set.add(str(ipaddress.ip_address(i)))
                l_ip_valid_a.append(str(ipaddress.ip_address(i)))
        except ValueError:
            pass
    return l_ip_valid_a

if __name__ == '__main__':
    print(extract_ip())
