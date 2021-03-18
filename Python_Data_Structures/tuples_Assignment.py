handle = open("mbox-short.txt")
lst = list()
lst2 = list()
lst3 = list()
count = dict()
for line in handle:
	if line.startswith("From "):
		lst = line.split()
		lst2 = lst[5].split(":")
		lst3.append(lst2[0])

# print(lst3)
for hour in lst3:
 	count[hour] = count.get(hour,0) + 1


# print(count)
lst = []
for key,val in count.items():
	lst.append((key,val))

# print(lst)

lst = sorted(lst)

# print(lst)

for key,val in lst:
	print(key,val)