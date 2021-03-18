friends = ["Rishikesh","Mangesh","Abhijit","Ram","Tejas","Vinayak","Pratik","Suraj","Roshan"]
print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of "print(friends)" ')
print(friends)

# print()

# values = [10,'ten',10.0000]
# print(values)

# print()

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of print(names) ')

names = [["Harish","Dadu"],["Pratik","Amol"],"Vinayak",["Amit","Banty"],"Ram",["Abhijit","Pappya"]]
print(names)

# for x in names:
# 	print(x)

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of for x in names[0]:')
for x in names[0]:
	print(x)

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of print(len(names))')

print(len(names))

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of print(len(names[0]))')

print(len(names[0]))

print("\n\n")

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of for x in range(len(names)):')

for x in range(len(names)):
	print(x)


print("\n\n")

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of for x in range(len(names)):')

for x in range(len(names)):
	print(names[x])


#Lists are Mutable.

names[0][1] = "Bhurtya"
names[0].append("Dadu")

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of print(names[0])')

print("\n\n\n",names[0])

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of print(names)')

print("\n\n\n",names)

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of friend = names + friends')

friend = names + friends

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of ')

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of print(friend)')


print(friend)
print('Output of print("1",friends[:])')
print("1\n",friends[:])

print('Output of print("2",friends[4:8])')
print("2\n",friends[4:8])

print('Output of print("3",friends[:4])')
print("3\n",friends[:4])

print('Output of print("4",friends[4:])')
print("4\n",friends[4:])

print("-------------+-------------+----------------+----------------+--------------------+-------------+---------------+--------------")
print('Output of names.append("Ajay")')
names.append("Ajay")
print(names)

print("-------------+-------------+----------------+----------------in operator----------+-------------+----------------+-------------")
print("Ajay" in names)
print("Harish" in friend[0])
print("Abhijit" in names)
print("Abhijit" not in names)
print("Harish" not in friend[0])

print("-------------+-------------+----------------+----------------Sort function--------+--------------+-------------+---------------")
friends.sort()
print(friends)