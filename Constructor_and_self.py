#Constructor = Constructor is a method which is used to initilaze the state of object.
#It is same as class name.

class Computer():
	
	def __init__(self):
		self.name = "naveen"
		self.age = 23
	
	def compare(self,other):
		if self.age == other.age:
			return True
		else:
			return False
c1 = Computer()
c1.age = 30
c2 = Computer()
c2.age = 25

if c1.compare(c2):
	print("the are same")
else:
	print("they are diffrenet")

print(c1.name)
print(c2.name)