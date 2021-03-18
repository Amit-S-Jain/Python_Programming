file1 = open("filedemo.txt")
for x in file1:
	x = x.rstrip()
	if x.startswith('NET4'):
		print(x)