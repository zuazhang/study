# -*- coding: utf-8 -*-

tgthost = raw_input("Please enter the hosts you want to scan:");
hosts = []
for i in tgthost.split(','):
	hosts.append(str(i))


hosts