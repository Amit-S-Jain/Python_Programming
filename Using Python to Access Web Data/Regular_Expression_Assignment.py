import re
handle = open("data_for_re2.txt")
sumelements = 0;
count = 0
for line in handle:
	x = re.findall('[0-9]+',line)
	if x:
		for z in x:
			count = count + 1
			sumelements = sumelements + int(z)

print("The Count is : ",count)
print("Sum of Elements is : ",sumelements)
