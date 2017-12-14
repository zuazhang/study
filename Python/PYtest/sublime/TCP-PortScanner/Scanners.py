# -*- coding: utf-8 -*- 

import socket

tgthost = raw_input("Please enter the hosts you want to scan:");
hosts = []
for i in tgthost.split(','):
	hosts.append(str(i))

ports = [20,21,22,23,80,135,445,443,3389,8080]

def Scanner(host,port):
	try:
		print "[+] Connecting to " +host+":" + str(port)
		s = socket(AF_INET, SOCK_STREAM)
		s.connect((host,port))
		s.send('Primal Security \n')
		banner = s.recv(1024)
		if banner:
			print "[+]Port" + str(port) + "open: "+str(banner)
		s.close()
	except:pass



for host in hosts:
	for port in ports:
		Scanner(host,port)
