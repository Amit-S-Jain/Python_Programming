file = open("mbox-short.txt")
count = 0
lst = list()
for x in file:
	if x.startswith('From '):
		lst = x.split()
		count = count + 1
		print(lst[1])





print("There were", count, "lines in the file with From as the first word")
