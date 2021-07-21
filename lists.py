#lists- lists are used to store multiple values in single variables.

#this_list = ["banana","cherry","apple"]
#print(this_list)
#list items - list items are ordered, changable,and allow duplicate values.

#print(this_list[1])
#thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist1[:4]
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
this_list  = ['banana','blackcurrant','mango','tomoto']
newlist = []
for x in this_list:
	if 'a' in x:
		newlist.append(x)
print(this_list)