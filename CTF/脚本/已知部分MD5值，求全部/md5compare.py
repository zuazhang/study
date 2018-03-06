#- * -coding: UTF - 8 - * -
import random
import hashlib

x = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
def couplerandom(number):
    stringx = ''.join(random.choice(x) for i in range(number))
    if stringx.isalnum() == True:#判断是不是子母和数字的组合
        return stringx
def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
    # strncmp(sStr1, sStr2, n) 字符串制定长度比较
str1 = 'd9ddd1800f'
n = 10# print cmp(sStr1[0: n], str[0: n])

while True:
    str = md5(couplerandom(4))
    i = cmp(str1[0: n], str[0: n])
    if i == 0:
        print str
        break