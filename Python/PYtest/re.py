# -*-coding: utf-8 -*-
#python正则表达式

#re.match函数
'''
re.match(patterb,string,flags=0)
pattern : 匹配的正则表达式
string  : 要匹配的字符串
flags   : 标志位，用于控制正则表达式的匹配方式
			如：是否区分大小写，多行匹配等
匹配成功，re,match函数返回一个匹配的对象，否则返回none


'''

#实例：
import re

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchObj:
	print "matchObj.group() : ",matchObj.group()
	print "matchObj.group(1) : ",matchObj.group(1)
	print "matchObj.group(2) : ",matchObj.group(2)
else:
	print "no match"



#re.search方法
matchObj = re.search(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchObj:
	print "matchObj.group() : ",matchObj.group()
	print "matchObj.group(1) : ",matchObj.group(1)
	print "matchObj.group(2) : ",matchObj.group(2)
else:
	print "no match"

#re.match 与 re.search 的区别
'''
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，匹配失败。
函数返回none；而re.search匹配整个字符串，知道找到一个匹配

'''	
matchObj = re.match(r'dogs',line,re.M|re.I)
if matchObj:
	print "match------->matchObj.group():",matchObj.group()
else:
	print "no match!!!!"
matchObj = re.search('dogs',line,re.M|re.I)
if matchObj:
	print "search------>matchObj.group():",matchObj.group()
else:
	print "no search!!!!"
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
