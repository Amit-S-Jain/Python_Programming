fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    # print(line)
    count = count + 1;
    start = line.find(":")
    val = line[start+1:]
    val = float(val)
    total = total + val
print("Average : ",(total/count))
