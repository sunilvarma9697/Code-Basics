#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#continue

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    continue
#else

fruits1 = ["apple", "banana", "cherry"]
y = ["mango" , "blackcurrant", 'grapes']
for x in fruits:
  print(x)
else:
	print(y)

#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)