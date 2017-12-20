# -*-coding: utf-8 -*-
import sys
from lib.core.Spider import SpiderMain

def main():
	root = "http://www.shiyanlou.com/"
	threadNum = 10
	#spider
	w = SpiderMain(root,threadNum)
	w.craw()

if __name__ == '__main__':
	main()
	