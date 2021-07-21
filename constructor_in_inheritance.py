#Constructor in inheritence
class A:
	def __init__(self):
		print("in A init")

	def feature1(self):
		print("Feature 1 is working")
	def feature2(self):
		print("Featrue 2 is working")

class B:
	def __init__(self):
		print("in B init")
	def feature1(self):
		print("Feature 3 is working")

	def feature4(self):
		print("Feature 4 is working")
class C(A,B):
	def __init__(self):
		super().__init__()
		print("in c init")
a1 = C()
a1.feature1()			

