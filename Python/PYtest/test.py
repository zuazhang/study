# -*- coding: utf-8 -*-
#if else
score = 55
if score >= 60:
    print 'passed'
else:
    print 'failed'
#if elif   此关键字与其他语言中的if ，else if相同
age = 18
if age >= 18:
    print 'adult'
elif age >=6:
    print 'teenager'
elif age >= 3:
    print 'kid'
else:
    print 'baby'
#for循环打印list中的元素
print u'for循环打印list中的元素'
l = [75,85,95,99]
sum = 0.0
for score in l:
    sum = sum + score
print sum/4
#while循环
N = 10
x = 0
while x < N:
    print x
    x = x + 1 
#利用while循环计算一百以内奇数的和
print u'利用while循环计算一百以内奇数的和'
sum = 0
x = 1
while x < 100:
    sum = sum + x
    x = x + 2
print sum 
#利用while True死循环配合break语句计算1+2+4+8....前20项的计算结果
print u'利用while True死循环配合break语句计算1+2+4+8....前20项的计算结果'
sum = 0
x = 1
n = 1
while True:
    sum = sum + x
    x =x * 2
    n = n + 1
    if n > 20:
        break
print sum 
#对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
print u'对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：'
sum = 0 
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum + x
print sum
#对一百以内的两位数使用两重循环打印十位数小于个位数的所有数
print u'对一百以内的两位数使用两重循环打印十位数小于个位数的所有数'
for x in [1,2,3,4,5,6,7,8,9,]:
    for y in [1,2,3,4,5,6,7,8,9,]:
	    if x < y:
		    print x*10+y

#我们把名字称为key，对应的成绩称为value，dict就是通过 key 来查找 value。
d = {
    'adam':80,
    'lisa':90,
    'bart':88,
    'paul':85
}
print(len(d))
print d['adam']
print d.get('sama')
print 'adam:',d['adam']
print 'lisa:',d.get('lisa')
str = input("input:\n")
for i in d:
    if d.get(i)==str:
	    print i
