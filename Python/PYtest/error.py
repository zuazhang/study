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
#����try�����׳�һ���쳣���Լ�ִ��finally�����
#finall���еĴ���ִ�к��쳣���ٴ��������ִ��except����
'''
try:
	fh = open("testfile","w")
	try:
		fh.write("this is my test file for exception handing !!")
	finally:
		print "going to close the file "
		fh.close()
except IOError:
	print "Error : can\'t find file or read data "
'''


#�쳣�Ĳ���
'''
һ���쳣���Դ��ϲ���������Ϊ������쳣��Ϣ����
����ʹ��except����������쳣�Ĳ���
�������ܵ��쳣ֵͨ���������쳣������С�
��Ԫ��ı��б������Խ���һ�����߶��ֵ
Ԫ��ͨ�����������ַ������������֣�����λ��
'''
#����Ϊ�����쳣��ʵ��
#�����ﶨ��һ������
'''
def temp_convert(var):
	try:
		return int(var)
	except ValueError,Argument:
		print "the argument does not contain numbers\n",Argument
#���ú���
temp_convert("xyz");
'''

#�����쳣
'''
���ǿ���ʹ��raise����Լ������쳣
һ���쳣������һ���ַ���������߶���python�ں��ṩ���쳣���������ʵ��������
����һ�����ʵ������
'''
#����һ���쳣
def functionName(level):
	if level < 1:
		raise "Invalid level !",level
'''
ע�⣺Ϊ���ܹ������쳣��except����������ͬ���쳣���׳����������ַ���
�������ǲ��������쳣
except "Invalid level !":

'''


#�û��Զ����쳣
'''
ͨ������һ���µ��쳣�࣬����������������Լ����쳣�ࡣ
�쳣Ӧ���ǵ��͵ļ̳���Exception�࣬ͨ��ֱ�ӻ��ӵķ�ʽ

����Ϊ��RuntimeError��ص�ʵ����ʵ���д�����һ���࣬����Ϊ
RuntimeError�������쳣����ʱ����������Ϣ

��try����У��û��Զ�����쳣��ִ��except��䣬����e�����ڴ���
Networkerror���ʵ��
'''
class Networkerror(RuntimeError):
	def _init_(self,arg):
		self.args = arg
#�������쳣
try:
	raise Networkerror("Bad hostname")
except Networkerror,e:
	print e.args





















	












