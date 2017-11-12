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


























