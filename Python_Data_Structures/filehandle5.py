#Count the Nmuber of lines in any file
filename = input("Enter the File Name: ")
fileopen = open(filename)
countl = 0;
countc = 0;
for x in fileopen:
	countl = countl + 1
	for y in x:
		countc = countc + 1;

print("Nmuber of Lines: ", countl)
print("Nmuber of Characters: ", countc)