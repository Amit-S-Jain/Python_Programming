import re
x = "My 2 favorite Numbers are 19 and 22"
y = re.findall('[0-9]+',x)
for i in range(len(y)):
	y[i] = int(y[i])
print(y)


z = re.findall('[0-9]+[0-9].+[and].+[0-9]+[0-9]',x)
print(z)


z = re.findall('^M.+?[ ].+?[ ]',x)
print(z)


z = re.findall('a.\S+',x)
print(z)