# -*- coding: utf-8 -*-
'''
python里的目录
所有文件都包含在各个不同的目录下，
mkdir()方法
在当前目录下创建新的目录。需要提供一个包含了要创建的目录名称的参数
'''
import os
os.mkdir("test")
'''
chdir()方法，来改变当前的目录。
需要的参数是你想设成当前目录的目录名称
我将此处注释，不执行这段代码
'''
#import  os
#将当前目录改为"/home/newdir"
#os.chdir("")
'''
getcwd()方法显示当前的工作目录
'''
os.getcwd()
'''
rmdir()方法删除目录，目录名称以参数传递
再删除这个目录之前，他的所有内容应该先被清楚
'''
#删除 "test"目录
#os.rmdir("test")













