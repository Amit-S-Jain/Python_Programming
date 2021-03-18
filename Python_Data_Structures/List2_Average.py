numlist = list()
while(True):
	x = input("Enter a Number: ")
	if(x=='done'):break
	x = float(x)
	numlist.append(x)

average = sum(numlist)/len(numlist)
print(average)