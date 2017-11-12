# -*- coding: utf-8 -*-
'''
python异常处理
python提供了两个非常重要的功能来处理python程序在运行中出现的异常和错误

什么是异常？
异常即是一个事件，该事件会在程序执行过程中发生，影响程序的正常运行
一般情况下，在python无法正常处理一个程序时就会发生异常
异常是python对象，表示一个错误
当python脚本发生异常时，我们需要捕获处理它，否则程序会终止执行

异常处理
捕捉异常可以使用try/except语句
该语句用来检测try语句中的错误，从而让except语句捕获异常信息并处理

'''
#下面是个简单的例子，他打开一个文件，在文件写入内容，且并未发生异常
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

#下面是一个简单的例子，打开一个文件在文件中写入内容，但文件没有写入权限
#发生异常
'''
try:
	fh = open("testfile","r")
	fh.write("this is my test file exception handing!!!")
except IOError:
	print "error: can\'t fine file or read data"
else:
	print "written content in the file successfully"
'''

#可以不带任何异常类型使用except，也可以带多种异常类型
#try-finally语句
'''
你可以使用except语句或者finally语句，但是两者不能同时使用
else语句也不能与finally语句同时使用
'''
#try-finally语句实例
'''
try:
	fh = open("testfile","w")
	fh.write("this is my test file foer exception handing!!")
finally:#退出时总会执行
	print "Error: can\'t find file or read data "
'''
#同样的例子可以写成如下形式
#当在try块中抛出一个异常，以及执行finally块代码
#finall块中的代码执行后，异常被再次提出，并执行except代码
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


#异常的参数
'''
一个异常可以带上参数，可作为输出的异常信息参数
可以使用except语句来捕获异常的参数
变量接受的异常值通产包含在异常的语句中。
在元祖的表单中变量可以接受一个或者多个值
元祖通常包含错误字符串，错误数字，错误位置
'''
#以下为单个异常的实例
#在这里定义一个函数
'''
def temp_convert(var):
	try:
		return int(var)
	except ValueError,Argument:
		print "the argument does not contain numbers\n",Argument
#调用函数
temp_convert("xyz");
'''

#触发异常
'''
我们可以使用raise语句自己触发异常
一个异常可以是一个字符串，类或者对象。python内核提供的异常，大多数是实例化的类
这是一个类的实例参数
'''
#定义一个异常
def functionName(level):
	if level < 1:
		raise "Invalid level !",level
'''
注意：为了能够捕获异常，except语句必须用相同的异常来抛出类对象或者字符串
例如我们捕获以上异常
except "Invalid level !":

'''


#用户自定义异常
'''
通过创建一个新的异常类，程序可以命名他们自己的异常类。
异常应该是典型的继承自Exception类，通过直接或间接的方式

以下为与RuntimeError相关的实例，实例中创建了一个类，基类为
RuntimeError用于在异常触发时输出更多的信息

在try语句中，用户自定义的异常后执行except语句，变量e是用于创建
Networkerror类的实例
'''
class Networkerror(RuntimeError):
	def _init_(self,arg):
		self.args = arg
#触发该异常
try:
	raise Networkerror("Bad hostname")
except Networkerror,e:
	print e.args





















	












