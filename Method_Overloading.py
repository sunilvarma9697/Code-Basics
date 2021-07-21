#Method Overloading - Two methods with same name and different Parameters or arguments is called method_overloading
#method overrding - methos with same name and same paarameters is called method_overriding.

class Student:
	def __init__(self,m1,m2):
		self.m1 = m1
		self.m2 = m2

	def sum(self,a = None,b = None,c = None):
		s = 0
		if a!=None and b!=None and c!=None:
			s = a + b + c

		elif a!=None and b!=None:
			s = a + b
		else:
			s = a

		return s

s1 = Student(58,69)
print(s1.sum(5))
