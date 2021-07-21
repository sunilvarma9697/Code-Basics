#Bubble sort :- bubble sort  is a stright forward method it is used to repeating and swapping the adjecent   
#elements they are not in right order.
# it compares elements at atime.#first element is greater than second then swap.

def sorts(nums):
	for i in range(len(nums)-1,0,-1):
		for j in range(i):
			if nums[j] > nums[j + 1]:
				temp = nums[j]
				nums[j] = nums[j + 1]
				nums[j + 1] = temp


nums= [5,3,4,6,8,7]
sorts(nums)
print(nums)