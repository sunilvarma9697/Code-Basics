#types of variables - 1. Instancec variable, 2.Static variable
#Instance variable
#Class variable

class Car:
	wheels = 4

	def __init__(self):
		self.milage = 10
		self.comapny = "BMW"

c1 = Car()
c2 = Car()

c1.milage = 3

Car.wheels = 4

print(c1.comapny,c1.milage,c1.wheels)
print(c2.comapny,c2.milage,c2.wheels)