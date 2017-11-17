# -*- coding: utf-8 -*-
import urllib,urllib2
#获取网页源代码
url = 'http://www.baidu.com'
r = urllib.urlopen(url)
#print r.read()
#urllib.urlretrieve()下载方法
#urllib.urlretrieve('http://labfile.oss.aliyuncs.com/courses/761/w8ay_1.zip',filename='F:/git/demo1/Python/PYtest/baidu.zip')