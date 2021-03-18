handle = open("mbox-short.txt")
lst = list()
lst2 = list()
count = dict()
for line in handle:
	if line.startswith("From "):
		lst = line.split()
		lst2.append(lst[1])

for email in lst2:
	count[email] = count.get(email,0) + 1
maxkey = 0
maxval = 0
for key,value in count.items():
	if value > maxval:
		maxval = value
		maxkey = key

print(maxkey,maxval)