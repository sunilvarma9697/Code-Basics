#Inner Class: class inside of a another class is called Inner class.
class Student:
	def __init__(self,name,rollno):
		self.name = name
		self.rollno = rollno
		self.lap = self.Laptop()

	def show(self):
		print(self.name,self.rollno)
		self.lap.show()



	class Laptop:
		def __init__(self):
			self.bramd = "HP"
			self.cpu = "i5"
			self.ram = 8
		def show(self):
			print(self.bramd,self.cpu,self.ram)

s1 = Student('naveen',2)
s1.show()
