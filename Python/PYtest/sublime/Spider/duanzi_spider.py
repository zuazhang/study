# -*- coding: utf-8 -*-

import re 
import urllib2

class Spider:
	'''
	内涵段子爬虫类
	'''
	def __init__(self):
		#在这里定义爬虫类所需要的基本属性
		self.enable = True #是否继续加载页面
		self.page = 1      #当前应该爬第几章页面

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
		response = urllib2.urlopen(req)
		html = response.read()
		#gbk_html = html.decode('gbk').encode('utf-8')
		pattern = re.compile(r'<div>.*?class="f18 mb20">(.*?)</div>',re.S)
		item_list = pattern.findall(html)

		return item_list
	def printOnePage(self,item_list,page):
		'''
		@brief 处理得到的段子列表
		@param item_list 得到的段子列表
		@param page 	 处理第几页
		'''
		print "*******第%d页爬取完毕...*******"%page
		for item in item_list:
			#print "================"
			item = item.replace("<p>","").replace("</p>","").replace("</br>","")
			self.writeFile(item)
	def writeFile(self,text):
		'''
		@brief 将数据追加写进文本
		@param text 文件内容
		'''
		myFile = open("./MyStory.txt",'a')#追加形式打开文件
		myFile.write(text)
		myFile.write("-------------------------------------")
		myFile.close()

	def doWork(self):
		'''
		让爬虫开始工作
		'''
		while self.enable:
			try:
				item_list = self.loadPage(self.page)
			except urllib2.URLError,e:
				print e.reason
				continue
			#对得到的item_list处理
			self.printOnePage(item_list,self.page)
			self.page += 1
			print "按回车继续..."
			print "输入quit退出"
			command = raw_input()
			if (command == "quit"):
				self.enable = False
				break






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
	mySpider.doWork()




