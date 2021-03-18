file = open("romeo.txt")
lst = list()
lst2 = list()
for x in file:
	lst2 = x.split()
	for z in lst2:
		if z not in lst:
			lst.append(z)



lst.sort()
print(lst)