# -*-coding: utf-8 -*-
'''
创建该函数的目的是为了将url中的参数进行替换
如：https://www.shiyanlou.com/courses/?a=1&b=2&c=3
中的1,2,3都取出来进行替换，所以创建这个函数来分割这些文本

这个函数会返回一个元组将每个参数用my_Payload标记，到时候
替换这个参数就行了

'''
import urlparse
import socket



def urlsplit(url):
	domain = url.split("?")[0]
	_url = url.split("?")[-1]
	pararm = {}
	for val in _url.split("&"):
		pararm[val.split("=")[0]] = val.split("=")[-1]

	#combine
	urls = []
	for val in pararm.values():
		new_url = domain + _url.replace(val,"my_Payload")
		urls.append(new_url)
	return urls

def gethostbyname(url):
	domain = urlparse.urlparse(url)
	#domain.netloc
	if domain.netloc is None:
		return None

	ip = socket.gethostbyname(domain.netloc)
	return ip


