# -*- coding: utf-8 -*- 
import urllib2

url = "http://www.baidu.com"
#我们要伪装的user_agent头
user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
#创建一个字典，使请求中的headers中的‘user_agent’对应我们伪装的ueser_agent
headers = {
	
	'User_Agent':user_agent
}
#新建一个请求
req = urllib2.Request(url,headers = headers)

response = urllib2.urlopen(req)
the_page = response.read()
print the_page



