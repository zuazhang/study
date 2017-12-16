# -*- coding: utf-8 -*- 

import socket
from threading import *




screenLock = Semaphore(value=1)


def portScan(host,ports):
	try:
		tgtIP = socket.gethostbyname(host)
	except:
		print "[-] Cannot Resolve'%s': Unknown host"% host
		return
	try:
		tgtName = socket.gethostbyaddr(tgtIP)
		print '\n[+] Scan Results for: '+ tgtNmae[0]
	except:
		print '\n[+] Scan Results for: '+ tgtIP
	socket.setdefaulttimeout(1)
	for port in ports:
		t = Thread(target=Scanner,args=(host,int(port)))
		t.start()



def Scanner(host,port):
	try:

		s = socket.socket()
		s.connect((host,port))
		s.send('Primal Security \n')
		banner = s.recv(1024)
		if banner:
			screenLock.acquire()
			print "[+] Connecting to " +host+":" + str(port)
			print "[+]Port" + str(port) + "open: "
			print "[+]>>>"+str(banner)	
	except:
		screenLock.acquire()
		print "[+] Connecting to " +host+":" + str(port)
		print "[-]Port" + str(port) + "closed\n"
	finally:
		screenLock.release()
		s.close()

def main():
	tgthost = raw_input("Please enter the hosts you want to scan:");
	hosts = []
	for i in tgthost.split(','):
		hosts.append(str(i))

	ports = [20,21,22,23,80,135,443,445,3389,8080]
	for host in hosts:
		portScan(host,ports)

if __name__ == '__main__':
	main()

