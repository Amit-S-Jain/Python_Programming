string = "I love India"
lst = string.split()
print(lst)
print(len(string))
print(len(lst))
for x in lst:
	print(x)


#If string doesn't have spaces:
string2 = "I;Love;India"
lst2 = string2.split()
print(lst2)
lst3 = string2.split(';')
print(lst3)
