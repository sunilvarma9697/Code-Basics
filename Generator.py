#Generator = it is used to create your own iterator and it is special type of functtion and it does not returns single value.
#yield keyword is used rather than return.

def Topten():

	n  = 1

	while n <= 10:
		sq = n * n
		yield sq
		n += 1
values = Topten()

for i in values:
	print(i)