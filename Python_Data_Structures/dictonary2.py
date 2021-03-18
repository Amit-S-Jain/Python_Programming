count = dict()
names = ["Amit","Harish","Mangesh","Amit","Harish","Vinayak","Harish","Amit","Vishal","Mangesh","Harish"]

for name in names:
	if name not in count:
		count[name] = 1
	else:
		count[name] = count[name] + 1

print(count)

for x in names:
	print(x)