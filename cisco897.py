#!/usr/bin/env python

from netmiko import ConnectHandler

cisco897 = {
'device_type': 'cisco_ios',
'ip': '192.168.50.254',
'username': 'hale',
'password': 'wuhao3101561',
}

conn1 = ConnectHandler(**cisco897)
outp = conn1.send_command("show run")
print (outp)