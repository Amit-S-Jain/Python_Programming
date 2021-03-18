names = ["Amit","Harish","Mangesh","Amit","Harish","Vinayak","Harish","Amit","Vishal","Mangesh","Harish"]
cnt = dict()
for name in names:
	cnt[name] = cnt.get(name,0) + 1
print("\n\n cnt")
print(cnt)


print(cnt.keys())
print(cnt.values())
print(cnt.items())

for key,value in cnt.items():
	print(key,value)