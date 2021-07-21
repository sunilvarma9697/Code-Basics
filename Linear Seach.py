#linear search  = Linear search is a method of finding elements within a list. It is also called a sequential search.
pos = -1
def Linear_search(list,n):
	i = 0

	while i < len(list):
		if list[i] == n:
			globals()['pos'] = i
			return True
		i = i + 1

	return False

list = [2,4,6,8,0,3,5,7,9]
n = 8
if Linear_search(list,n):
	print("found")
else:
	print("not found ")