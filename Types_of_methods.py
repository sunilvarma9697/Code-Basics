#Types of methods = 1.Instance method, Static method, Class method.

class Student:

	school = 'Telusko'

	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):
		return (self.m1 + self.m2 + self.m3)/3

	@classmethod

	def getschool(cls):
		return cls.school



	@staticmethod
	def info():
		print("This is a Static method declearing static variable")


s1 = Student(34,36,45)
s2 = Student(24,25,26)


print(s1.avg())
print(Student.info())