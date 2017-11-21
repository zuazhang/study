# -*- coding: utf-8 -*- 
import socket
socket.setdefaulttimeout(2)
s = socket.socket()
d.connect(("100.64.24.155",21))
ans = s.recv(1024)
print ans
