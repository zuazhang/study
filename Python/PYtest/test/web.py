# -*- coding: utf-8 -*-
import urllib,urllib2
#��ȡ��ҳԴ����
url = 'http://www.baidu.com'
r = urllib.urlopen(url)
print r.read()
#urllib.urlretrieve()�����ļ�������urllib�⣩
#urllib.urlretrieve('http://labfile.oss.aliyuncs.com/courses/761/w8ay_1.zip',filename='F:/git/demo1/Python/PYtest/baidu.zip')
#urllib2.Requests()  ��������ͷ



