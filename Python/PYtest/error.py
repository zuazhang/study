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















