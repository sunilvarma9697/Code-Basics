#Variables - variables are containers there are storing the value
x = 2
y = 3
z = x + y;
print(z)

name  = "Youtube"

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(name + " Rocks")


#global variables - created outside of a function and also inside function.

x = "Awsome"
def myfun():
	print("program is " + x);
myfun()
print(id(x))



