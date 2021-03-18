#Count the Nmuber of lines in any file with try Catch Block
filename = input("Enter the File Name: ")

try:
	fileopen = open(filename)
except :
	print("Sorry, File Not Available!!!")
	quit()
countl = 0
countc = 0
for x in fileopen:
	countl = countl + 1
	for y in x:
		countc = countc + 1;

print("Nmuber of Lines: ", countl)
print("Nmuber of Characters: ", countc)