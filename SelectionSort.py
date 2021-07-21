#Selection sort:-  algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) 
# from unsorted part and putting it at the beginning.

def Selection_sort(nums):
	
	for i in range(5):
		minpos = i

		for j in range(i,6):
			if nums[j] < nums[minpos]:
				minpos = j

		temp = nums[i]
		nums[i] = nums[minpos]
		nums[minpos] = temp
		print(nums)

nums = [4,6,9,3,5,7,]
Selection_sort(nums)
print(nums)