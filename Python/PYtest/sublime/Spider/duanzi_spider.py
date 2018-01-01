# -*- coding: utf-8 -*-

import re 
import urllib2

class Spider:
	'''
	内涵段子爬虫类
	'''
	def loadPage(self,page):
		'''
		@brief 定义一个url请求
		@param page 需要请求的第几页
		@returns  返回的html页面
		'''
		url = 'http://www.neihan8.com/article/list_5_'+str(page)+'.html'
		user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0'
		headers = {'User-Agent' : user_agent}
		req = urllib2.Request(url,headers = headers)
		response = urllib2.urlopen(url)
		html = response.read()
		#gbk_html = html.decode('gbk').encode('utf-8')
		pattern = re.compile(r'<div>.*?class="f18 mb20">(.*?)</div>',re.S)
		item_list = pattern.findall(html)

		return item_list

if __name__ == '__main__':
	print '''
	=========================
		内涵段子小爬虫
	=========================
	'''
	print u'请按下回车开始'
	raw_input()

	#定义一个spider对象
	mySpider = Spider()
	mySpider.loadPage(1)




