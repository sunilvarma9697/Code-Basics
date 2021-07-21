#Polymorphism - it is nothing but assigning the behaviour or value of a Sub class that already declared in main class.
class Computer:
	def execute(self):
		print("Compiling")
		print("Running")

class MyEditor:
	def execute(self):
		print("Spell check")
		print("convertion check")
		print("compiling")
		print("running")

class Laptop:

	def code(self,ide):
		ide.execute()

ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)
