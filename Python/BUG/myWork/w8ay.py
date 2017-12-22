# -*-coding: utf-8 -*-
import sys
from lib.core.Spider import SpiderMain
from lib.core import webcms
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
	root = "https://blog.yesfree.pw/"
	threadNum = 10
	#webcms
	ww = webcms.webcms(root,threadNum)
	ww.run()

	#spider
	w = SpiderMain(root,threadNum)
	w.craw()




if __name__ == '__main__':
	main()
	