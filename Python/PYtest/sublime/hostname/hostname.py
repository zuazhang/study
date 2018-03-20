# -*- coding: utf-8 -*-
import socket 
hostname = socket.gethostname()

ip = socket.gethostbyname(hostname)
'''
ipList = socket.gethostbyname_ex(hostname)

print ipList
'''
print hostname + ip
print type(hostname)
print type(ip)