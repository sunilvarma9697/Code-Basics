a =10
print(id(a))

def somthing():
	a = 9
	x = globals()['a']
	print(id(x))
	print("value of x",x)
somthing()
