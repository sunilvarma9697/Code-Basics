#Fibonacci - Fabonacci is set of numbers that are starts with zero and one.
def fib(n):
	a = 0
	b  = 1
	if n == 1:
		print(a)

	print(a)
	print(b)
	for i in range(2,n):
		c = a + b 
		a = b
		b = c
		print(c)

fib(10)