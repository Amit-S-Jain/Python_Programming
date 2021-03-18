fileO = open ("filedemo.txt")
count = 0
for x in fileO:
	for j in x:
		count = count + 1

print(count)