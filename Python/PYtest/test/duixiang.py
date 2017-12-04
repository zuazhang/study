# -*- coding: utf-8 -*-
'''
������������:
�ࣺ
	��������������ͬ���Ժͷ����Ķ���ļ��ϡ������˸ü�����ÿ�����������е�
	���Ժͷ��������������ʵ��
�������
	����������ʵ�����Ķ������ǹ��õġ�������������������ں�����֮�⣬��
	����ͨ������Ϊʵ������ʹ��
���ݳ�Ա��
	���������ʵ���������ڴ����༰��ʵ��������������
�������أ�
	������׼̳еķ�������������������󣬿��Զ�����и�д��������̽�����
	���ĸ��ǣ�override����Ҳ��Ϊ����������
ʵ��������
	�����ڷ����еı�����ֻ�����ڵ�ǰʵ������
�̳У�
	��һ�������ࣨderived class���̳л��ࣨbase class�����ֶκͷ������̳�Ҳ
	�����һ��������Ķ�����Ϊһ���������Դ������磺
	һ��Dog���͵Ķ���������Animal�࣬����ģ�⡰��һ����is-a������ϵ��Dog��һ��
	Animal��
ʵ������
	����һ�����ʵ������ľ������
������
	���ж���ĺ���
����
	ͨ���ඨ������ݽṹʵ������������������ݳ�Ա���������ʵ���������ͷ���
'''
#������
#ʹ��class���������һ������
class Employee:
	'Common base class for all employees'#���ĵ��ַ���
	empCount = 0
	#���������޿ո���»���
	def __init__(self,name,salary):
		self.name = name 
		self.salary = salary
		Employee.empCount += 1
		
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
		
	def displayEmployee(self):
		print "Name : ",self.name, ", Salary: ", self.salary
#���ｫ����Employee��ĵ�һ��ʵ��
emp1 = Employee("Zara", 2000)
#�ڶ���ʵ��
emp2 = Employee("manni", 5000)
#���ʶ��������
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
emp1.age = 7#���һ��age����
del emp1.age #ɾ��age����
'''
hasattr(emp1, 'age')    # ������� 'age' ���Է��� True��
getattr(emp1, 'age')    # ���� 'age' ���Ե�ֵ
setattr(emp1, 'age', 8) # ������� 'age' ֵΪ 8
delattr(empl, 'age')    # ɾ������ 'age'
'''
#################################
##python����������
##ʵ�����£�
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
#����ĵ��ַ���		
print "Employee2.__doc__: ",Employee2.__doc__
#����
print "Employee2.__name__: ",Employee2.__name__
#�ඨ�����ڵ�ģ��
print "Employee2.__module__: ",Employee2.__module__
#������и��๹��Ԫ��
print "Employee2.__bases__: ",Employee2.__bases__
#�������
print "Employee2.__dict__: ",Employee2.__dict__


###################################################################

#python �������٣��������գ�

###################################################################��
'''
ͬJava����һ����Pythonʹ�������ü�����һ�򵥼�����׷���ڴ��еĶ���
��Python�ڲ���¼������ʹ���еĶ�����ж������á�

һ���ڲ����ٱ�������Ϊһ�����ü�������

�����󱻴���ʱ�� �ʹ�����һ�����ü���,�������������Ҫʱ,Ҳ����˵��
�����������ü�����Ϊ0 ʱ�������������ա����ǻ��ղ���"����"�ģ��ɽ�
�������ʵ���ʱ��������������ռ�õ��ڴ�ռ���ա�

�������ջ��Ʋ���������ü���Ϊ0�Ķ���ͬ��Ҳ���Դ���ѭ�����õ������
ѭ������ָ���ǣ����������໥���ã�����û�����������������ǡ��������
�£���ʹ�����ü����ǲ����ġ�Python �������ռ���ʵ������һ�����ü�����
��һ��ѭ�������ռ�������Ϊ���ü����Ĳ��䣬�����ռ���Ҳ�����ı������
�����ܴ󣨼�δͨ�����ü������ٵ���Щ���Ķ��� ����������£���������
��ͣ��������ͼ��������δ���õ�ѭ���� 
'''
#��������__del__,�ڶ������ŵ�ʱ�򱻵��ã��������ٱ�ʹ��ʱ����������
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
print id(pt1),id(pt2),id(pt3)#��ӡ�����id
del pt1
del pt2
del pt3

#��ļ̳�
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
		
c = Child()        #ʵ��������
c.childMethod()    #��������ķ���
c.parentMethod()   #���ø���ķ���
c.setAttr(200)     #���ø���ķ���
c.getAttr()        #���ø���ķ���  

##########################################

###���ط���
# �����ĸ��෽���Ĺ��ܲ������������������������������㸸��ķ���
###���������
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
#�������ݣ�
'''
��python��ʵ���������غܼ򵥣�����Ҫ��ǰ���ʲô�ؼ��֣�ֻҪ���������
���Ա����ǰ��������»��߼���ʵ���������صĹ��ܣ��������������ʵ����
˵����������ͳ�Ա�����ǲ���ʹ�õģ���������ļ̳�����˵��Ҳ�����صģ�
��������̳�����Զ�����һģһ���ı��������Ա������������������������
ͻ��
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
Python������ʵ������������������ݣ��������ʹ��
object._className__attrName�������ԣ������´�����
�����ϴ�������һ�д��룺
'''
print counter._JustCounter__secretCount







































