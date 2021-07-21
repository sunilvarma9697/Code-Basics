#Pass list into a function

def count(lst):
	even  = 0
	odd   = 0

	for i in lst:
		if i % 2  == 0:
			even += 1
		else:
			odd += 1
	return even , odd

lst = [22,23,25,24,21,36,42,27,29]

even , odd = count(lst)
print(even)
print(odd)

print("Even :{} and odd :{}".format(even,odd))