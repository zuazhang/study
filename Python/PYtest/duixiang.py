# -*- coding: utf-8 -*-
'''
面向对象技术简介:
类：
	用来描述具有相同属性和方法的对象的集合。定义了该集合中每个对象所共有的
	属性和方法，对象是类的实例
类变量：
	类变量在真个实例化的对象中是公用的。类变量定义在类中且在函数体之外，类
	变量通常不做为实例变量使用
数据成员：
	类变量或者实例变量用于处理类及其实例对象的相关数据
方法重载：
	如果弗雷继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫做方
	法的覆盖（override），也称为方法的重载
实例变量：
	定义在方法中的变量，只作用于当前实例的类
继承：
	即一个派生类（derived class）继承基类（base class）的字段和方法。继承也
	允许把一个派生类的对象作为一个基类对象对待。例如：
	一个Dog类型的对象派生自Animal类，这是模拟“是一个（is-a）”关系（Dog是一个
	Animal）
实例化：
	创建一个类的实例，类的具体对象
方法：
	类中定义的函数
对象：
	通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法
'''
#创建类
#使用class语句来创建一个新类
class Employee:
	'Common base class for all employees'#类文档字符串
	empCount = 0
	#两个连续无空格的下划线
	def __init__(self,name,salary):
		self.name = name 
		self.salary = salary
		Employee.empCount += 1
		
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
		
	def displayEmployee(self):
		print "Name : ",self.name, ", Salary: ", self.salary
#这里将创建Employee类的第一个实例
emp1 = Employee("Zara", 2000)
#第二个实例
emp2 = Employee("manni", 5000)
#访问对象的属性
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
emp1.age = 7#添加一个age属性
del emp1.age #删除age属性
'''
hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(empl, 'age')    # 删除属性 'age'
'''
#################################
##python内置类属性
##实例如下：
class Employee2:
	'Common base class for all employees'
	empCount = 0
	
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee2.empCount += 1
	
	def displayCount(self):
		print "Total Employee2 %d " % Employee2.empCount
		
	def displayEmployee2(self):
		print "Name : ",self.name, ",Salary : ", self.salary
#类的文档字符串		
print "Employee2.__doc__: ",Employee2.__doc__
#类名
print "Employee2.__name__: ",Employee2.__name__
#类定义所在的模块
print "Employee2.__module__: ",Employee2.__module__
#类的所有父类构成元素
print "Employee2.__bases__: ",Employee2.__bases__
#类的属性
print "Employee2.__dict__: ",Employee2.__dict__


###################################################################

#python 对象销毁（垃圾回收）

###################################################################、
'''
同Java语言一样，Python使用了引用计数这一简单技术来追踪内存中的对象。
在Python内部记录着所有使用中的对象各有多少引用。

一个内部跟踪变量，称为一个引用计数器。

当对象被创建时， 就创建了一个引用计数,当这个对象不再需要时,也就是说，
这个对象的引用计数变为0 时，它被垃圾回收。但是回收不是"立即"的，由解
释器在适当的时机，将垃圾对象占用的内存空间回收。

垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。
循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。这种情况
下，仅使用引用计数是不够的。Python 的垃圾收集器实际上是一个引用计数器
和一个循环垃圾收集器。作为引用计数的补充，垃圾收集器也会留心被分配的
总量很大（及未通过引用计数销毁的那些）的对象。 在这种情况下，解释器会
暂停下来，试图清理所有未引用的循环。 
'''
#析构函数__del__,在对象消逝的时候被调用，当对象不再被使用时，方法运行
class Point:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y 
	def __del__(self):
		class_name = self.__class__.__name__
		print class_name,"destroyed"

pt1 = Point()
pt2 = pt1
pt3 = pt2
print id(pt1),id(pt2),id(pt3)#打印对象的id
del pt1
del pt2
del pt3

#类的继承
class Parent:
	parentAttr = 100 
	def __int__(self):
		print "Calling parent constructor"
		
	def parentMethod(self):
		print "Calling parent method"
	
	def setAttr(self,attr):
		Parent.parentAttr = attr
		
	def getAttr(self):
		print "parent attribute :",Parent.parentAttr

		
class Child(Parent):
	def __init__(self):
		print "Calling child constructor"
		
	def childMethod(self):
		print 'Calling child method'
		
c = Child()        #实例化子类
c.childMethod()    #调用子类的方法
c.parentMethod()   #调用父类的方法
c.setAttr(200)     #调用父类的方法
c.getAttr()        #调用父类的方法  

##########################################

###重载方法
# 如果你的父类方法的功能不能满足你的需求，你可以在子类重载你父类的方法
###运算符重载
'''
class Vector:
	def __init__(self,a,b):
		self.a = a 
		self.b = b
		
	def __str__(self):
		return 'Vector (%d,%d)' % (self.a,self.b)
		
	def __add__(self):
		return Vector(self.a + other.a, self.b + other.b)
		
v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1+v2
'''
#隐藏数据：
'''
在python中实现数据隐藏很简单，不需要在前面加什么关键字，只要把类变量名
或成员函数前面加两个下划线即可实现数据隐藏的功能，这样，对于类的实例来
说，其变量名和成员函数是不能使用的，对于其类的继承类来说，也是隐藏的，
这样，其继承类可以定义其一模一样的变量名或成员函数名，而不会引起命名冲
突。
'''
class JustCounter:
	__secretCount = 0
	
	def count(self):
		self.__secretCount += 1
		print self.__secretCount
		
counter = JustCounter()
counter.count()
counter.count()
#print counter.__secretCount
'''
Python不允许实例化的类访问隐藏数据，但你可以使用
object._className__attrName访问属性，将如下代码替
换以上代码的最后一行代码：
'''
print counter._JustCounter__secretCount







































