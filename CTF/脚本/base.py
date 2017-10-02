# -*- coding: UTF-8 -*-
import base64

#base加密函数
def encode(str):
	a = base64.b64encode(str)
	b = base64.b32encode(str)
	c = base64.b16encode(str)
	print "base64 encode : "+a
	print "base32 encode : "+b
	print "base16 encode : "+c
#base解密函数
def decode(str):
	a = base64.b64decode(str)
	b = base64.b32decode(str)
	c = base64.b16decode(str)
	print "base64 decode : "+a
	print "base32 decode : "+b
	print "base16 decode : "+c

def choice_1():
	s = raw_input("please input the string what you want to encode:")
	encode(s)
def choice_2():
	s = raw_input("please input the Base_string what you want to decode:")
	decode(s)
print "please choice the option :\n1.encode the String\n2.decode the Base_string\n"
n = int(raw_input("please choice:"))
if n == 1:
	choice_1()
elif n == 2:
	choice_2()
else:
	print "Wrong !!!!\n please choice 1 or 2!!!!!"