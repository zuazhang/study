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


























