# -*-coding: utf-8 -*-
#python������ʽ

#re.match����
'''
re.match(patterb,string,flags=0)
pattern : ƥ���������ʽ
string  : Ҫƥ����ַ���
flags   : ��־λ�����ڿ���������ʽ��ƥ�䷽ʽ
			�磺�Ƿ����ִ�Сд������ƥ���
ƥ��ɹ���re,match��������һ��ƥ��Ķ��󣬷��򷵻�none


'''

#ʵ����
import re

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchObj:
	print "matchObj.group() : ",matchObj.group()
	print "matchObj.group(1) : ",matchObj.group(1)
	print "matchObj.group(2) : ",matchObj.group(2)
else:
	print "no match"



#re.search����
matchObj = re.search(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchObj:
	print "matchObj.group() : ",matchObj.group()
	print "matchObj.group(1) : ",matchObj.group(1)
	print "matchObj.group(2) : ",matchObj.group(2)
else:
	print "no match"

#re.match �� re.search ������
'''
re.matchֻƥ���ַ����Ŀ�ʼ������ַ�����ʼ������������ʽ��ƥ��ʧ�ܡ�
��������none����re.searchƥ�������ַ�����֪���ҵ�һ��ƥ��

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
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
