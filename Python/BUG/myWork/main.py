# -*-coding: utf-8 -*-
import sys
from lib.core.Spider import SpiderMain
from lib.core import webcms,common,PortScan,webdir,fun_until


reload(sys)
sys.setdefaultencoding('utf-8')

def main():
	root = "http://www.shiyanlou.com/"
	threadNum = 10
	#CDN check
	print "CDN checking...."
	msg,iscdn = fun_until.checkCDN(root)
	print msg
	if iscdn:
		#PortScan
		ip = common.gethostbyname(root)
		print "IP:",ip
		print "start Port Scan :"
		pp = PortScan.PortScan(ip)
		pp.work()

		#DIR fuzz
		dd = webdir.webdir(root,threadNum)
		dd.work()
		dd.output()


		#webcms
		ww = webcms.webcms(root)
		ww.run()

		#spider
		w = SpiderMain(root,threadNum)
		w.craw()




if __name__ == '__main__':
	main()
	