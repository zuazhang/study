# -*- coding: utf-8 -*-
'''
重命名和删除文件
python 的os模块提供了帮你执行文件操作的方法。比如重命名和删除文件
要使用这个模块，你必须先导入他，然后可以调用相关的各种功能
rename（） 方法：
需要两个参数：当前的文件名和新文件名

'''
import os
os.rename("test1.txt","test2.txt")