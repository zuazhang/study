# -*- coding: utf-8 -*-
'''
python�쳣����
python�ṩ�������ǳ���Ҫ�Ĺ���������python�����������г��ֵ��쳣�ʹ���

ʲô���쳣��
�쳣����һ���¼������¼����ڳ���ִ�й����з�����Ӱ��������������
һ������£���python�޷���������һ������ʱ�ͻᷢ���쳣
�쳣��python���󣬱�ʾһ������
��python�ű������쳣ʱ��������Ҫ��������������������ִֹ��

�쳣����
��׽�쳣����ʹ��try/except���
������������try����еĴ��󣬴Ӷ���except��䲶���쳣��Ϣ������

'''
#�����Ǹ��򵥵����ӣ�����һ���ļ������ļ�д�����ݣ��Ҳ�δ�����쳣
'''
try:
	fh = open("testfile","w")
	fh.write("this is my test file for exception handing!!!")
except IOError:
	print "ERROR: can\'t find file or read data"
else:
	print "written content in the file successfully"
	fh.close()
'''

#������һ���򵥵����ӣ���һ���ļ����ļ���д�����ݣ����ļ�û��д��Ȩ��
#�����쳣
'''
try:
	fh = open("testfile","r")
	fh.write("this is my test file exception handing!!!")
except IOError:
	print "error: can\'t fine file or read data"
else:
	print "written content in the file successfully"
'''

#���Բ����κ��쳣����ʹ��except��Ҳ���Դ������쳣����
#try-finally���
'''
�����ʹ��except������finally��䣬�������߲���ͬʱʹ��
else���Ҳ������finally���ͬʱʹ��
'''
#try-finally���ʵ��
'''
try:
	fh = open("testfile","w")
	fh.write("this is my test file foer exception handing!!")
finally:#�˳�ʱ�ܻ�ִ��
	print "Error: can\'t find file or read data "
'''
#ͬ�������ӿ���д��������ʽ

try:
	fh = open("testfile","w")
	try:
		fh.write("this is my test file for exception handing !!")
	finally:
		print "going to close the file "
		fh.close()
except IOError:
	print "Error : can\'t find file or read data "








	












