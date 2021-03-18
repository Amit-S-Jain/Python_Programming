file1 = open('filedemo.txt')
for x in file1:
	if x.startswith('NET4'):
		continue
	print(x)