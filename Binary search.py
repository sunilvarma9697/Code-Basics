#Binary search := A binary search is an algorithm to find a particular element in the list.
pos = -1

def Binary_search(list, n):

	l = 0
	u = len(list)-1

	while l <= u:
		mid = (l+u)//2

		if list[mid]  == n:
			globals()['pos'] = mid
			return True
		else:
			if list[mid] < n:
				l = mid + 1
			else:
				u = mid - 1
	return False
list = [2,4,6,8,9,23,45,56,78]
n = 87
if Binary_search(list,n):
	print("Found ",pos)
else:
	print("not found")
