from  functools import reduce
nums = [2,4,3,5,7,6,9,8,23,43]
evens = list(filter(lambda n:n %2 == 0,nums))
doubles = list(map(lambda n : n * 2,nums))
sum = reduce(lambda a,b : a + b,doubles)
print(doubles)
print(evens)
print(sum)