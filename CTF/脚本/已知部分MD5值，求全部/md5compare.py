#- * -coding: UTF - 8 - * -
import random
import hashlib

x = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
def couplerandom(number):
    stringx = ''.join(random.choice(x) for i in range(number))
    if stringx.isalnum() == True:#判断是不是子母和数字的组合
        return stringx
def md5jiami(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
    # strncmp(sStr1, sStr2, n) 字符串制定长度比较
str1 = 'f8a425493e'
#正确答案：f8a425493ee6d5513db4d774457108fe
n = 10# print cmp(sStr1[0: n], str[0: n])
print u"正在进行比对，请耐心等待。。。"

while True:
    #str2 = couplerandom(4)
    str = md5jiami(couplerandom(4))
    i = cmp(str1[0: n], str[0: n])
    if i == 0:
    	print u'==========================MD5值已找到==================================='
    	print '           '
        print '>>>>>>>>>>>>>>>>>>>>>      '+str
        #print '-----'+str2
        print '           '
        break