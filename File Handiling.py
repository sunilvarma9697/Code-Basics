#File handiling - it means handle the file to allow the users.

f = open('','r')
print(f.read)
print(f.readline())
print(f.readline(),end = "")
f1 = open('','w')
f1.write('Something')
f1.write("people")
f1.write('laptop')
f2 = open('','a')
f2.write('mobile')

for data in f:
	print(data)  #featching every thing.


