import re
handle = open("mbox-short.txt")
# for line in handle:
line = list()
for x in handle:
	z = re.findall('^From (\S+@\S+)',x)
	if  z:
		line.append(z[0])
print(line)