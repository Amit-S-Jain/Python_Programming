
#Opening File
counts = dict()
filename = input("Enter the file name = ")
handle = open(filename)
words = list()
#Seprating the words
for line in handle:
	words = words + line.split()


#Counting the words in Dictionary

for word in words:
	counts[word] = counts.get(word,0) + 1

# print(counts)
maxval = 0
maxkey = 0
for key,value in counts.items():
	if maxval < value:
		maxval = value
		maxkey = key

print(maxkey,maxval)