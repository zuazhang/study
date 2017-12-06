# -*- coding: utf-8 -*-
import urllib,urllib2
#获取网页源代码
url = 'http://www.baidu.com'
r = urllib.urlopen(url)
print r.read()
#urllib.urlretrieve()下载文件（属于urllib库）
#urllib.urlretrieve('http://labfile.oss.aliyuncs.com/courses/761/w8ay_1.zip',filename='F:/git/demo1/Python/PYtest/baidu.zip')
#urllib2.Requests()  定制请求头



