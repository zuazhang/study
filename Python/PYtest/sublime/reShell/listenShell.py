#coding:UTF-8
#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定443端口并监听任意地址的连接请求
s.bind(('0.0.0.0',443))
#最大挂起连接数
s.listen(2)
print "Listening on port 443....."
(client,(ip,port)) = s.accept()
print "Received connection from : ",ip

while True:
	command = raw_input('~$ ')
	encode = bytearray(command)
	for i in range(len(encode)):
		encode[i] ^= 0x41

	client.send(encode)
	en_data = client.recv(2048)
	decode = bytearray(en_data)
	for i in range(len(decode)):
		decode[i] ^= 0x41
	print decode

client.close()
s.close()
