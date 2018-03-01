# -*-coding: utf-8 -*-
import sys
from lib.core.Spider import SpiderMain
from lib.core import webcms,common,PortScan,webdir,fun_until,outputer

output = outputer.outputer()
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
	root = "http://www.shiyanlou.com/"
	domain = common.codog_urlparse(root)
	threadNum = 10
	#CDN check
	print "CDN checking...."
	iscdn = True
	try:

		msg,iscdn = fun_until.checkCDN(root)
		output.add("cdn",msg)
		output.build_html(domain)
		print msg
	except:
		print "[Error]:CDN check error!!!!!!!!!!"
	if iscdn:
		#PortScan
		ip = common.gethostbyname(root)
		print "IP:",ip
		print "start Port Scan :"
		pp = PortScan.PortScan(ip)
		pp.work()
		output.build_html(domain)

	#DIR fuzz
	dd = webdir.webdir(root,threadNum)
	dd.work()
	dd.output()
	output.build_html(domain)



	#webcms
	ww = webcms.webcms(root)
	ww.run()
	output.build_html(domain)


	#spider
	w = SpiderMain(root,threadNum)
	w.craw()




if __name__ == '__main__':
	main()
	