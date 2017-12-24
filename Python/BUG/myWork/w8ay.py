# -*-coding: utf-8 -*-
import sys
from lib.core.Spider import SpiderMain
from lib.core import webcms,common,PortScan

reload(sys)
sys.setdefaultencoding('utf-8')

def main():
	root = "http://blog.yesfree.pw/"
	threadNum = 10
	#PortScan
	ip = common.gethostbyname(root)
	print "IP:",ip
	print "start Port Scan :"
	pp = PortScan.PortScan(ip)
	pp.work()
	



	#webcms
	ww = webcms.webcms(root)
	ww.run()

	#spider
	w = SpiderMain(root,threadNum)
	w.craw()




if __name__ == '__main__':
	main()
	