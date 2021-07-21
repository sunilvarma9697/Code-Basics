#class - class is simply represented as type of an object and its is also called blueprint.
#object - object is termed as instance of a class and it has own state.
class Computer(object):
	"""docstring for Computer"""
	def config(self):
		print("i5, 16GB, 1TB")

com1 = Computer()
com1.config()
	
