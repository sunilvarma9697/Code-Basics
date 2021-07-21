#Type of Arguments - Formal Arguments and Actual Arguments

def Add(a,b):
	c = a + b;
	print(c)
Add(5,6)

def Person(name,age):
	print(name);
	print(age);
Person("kumar",22) 

def sum(a,*b):
	c = a
	for i in b:
		c = c + i
	print(c)
sum(2,34,5,67,77)