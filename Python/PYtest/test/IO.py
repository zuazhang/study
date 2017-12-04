# -*- coding: utf-8 -*-
#python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘

#raw_input 函数
str = raw_input("enter your input :");
print "received input is :",str

#input 函数
#input 函数和 raw_input 函数基本可以互换，但是input函数会假设你输入的是
#一个有效的python表达式，并返回结果

str_1 = input("enter your input : ");
print "received input is :",str_1

#如何读写实际的数据文件
#python提供了必要的函数和方法进行默认情况下的文件基本操作

#open函数
#你必须先用内置的函数open()打开一个文件，创建一个file对象，
#相关的辅助方法才可一调用它进行读写
#打开一个文件 
fo = open("foo.txt","wb")
print "name of the file :",fo.name#返回文件的名称
print "closed or not :",fo.closed#返回true，如果文件已被关闭，返回flase
print "opening mode :",fo.mode#返回被打开文件的访问模式
print "softspace flag :",fo.softspace#

#close方法。刷新缓冲区里任何还没有写入的信息，并关闭该文件，这之后便不能再写入
#当一个文件对象的引用被重新指定给另一个文件时，python会关闭之前的文件。
#用close（）方法关闭文件是一个很好的习惯

#关闭上文打开的文件
fo.close()

'''
Write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，python字符串
可以是二进制数据而不仅仅是文字
下端代码中的换行符“\n”，使用记事本打开文件时，并没有换行。但是用notepad++
打开时，有换行。
'''
fo = open("foo.txt","wb")
fo.write("python is a great language.\nYeah its great!!!\n");
fo.close()

'''
read()方法，从一个打开的文件中读取一个字符串，需要重点注意的是，python
字符串可以是二进制数据，而不仅仅是文字
该方法中传递的参数是要从已打开的文件中读取的字节计数。该方法从文件的
开头开始读取，如果没有传入参数，他会尽可能多的读取内容，很可能是知道文件的末尾

'''
fo = open("foo.txt","r+")#权限为读写
str_2 = fo.read(10);
print "readed string is : ",str_2
fo.close()
'''
文件位置：
tell（）方法告诉你文件内的当前位置，换句话说，下一次的读写会发生在文件开头
这么多字节之后：  seek(offset[,from])方法改变当前文件的位置，offset变量表表示
要移动的字节数，from变量指定开始移动字节的参考位置
如果from为0，这意味着将文件的开头作为移动字节的参考位置，如果设为1，则使用
当前的位置作为参考，如果设为2，那么该文件的末尾将作为参考位置
'''
fo = open("foo.txt","r+")
str_3 = fo.read(11);
print "read string is :",str_3

#查找当前位置
position = fo.tell();
print "current file position :",position
#把指针再次重定位到文件开头
position = fo.seek(0,0);
str_4 = fo.read(12);
print "again read string is :",str_4
fo.close()



































