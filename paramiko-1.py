#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2017/4/5
# Created by 独自等待
# 博客 http://www.waitalone.cn/
import paramiko

import time

hostname = '192.168.50.254'
port = 22
username = 'hale'
password = 'wuhao3101561'
client = paramiko.SSHClient()  # 绑定实例
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password, timeout=5)
remote_conn = client.invoke_shell()
remote_conn.send('terminal length 0\n')
time.sleep(1)
remote_conn.send('show run\n')
time.sleep(1)
output = remote_conn.recv(65535)
print (output)
