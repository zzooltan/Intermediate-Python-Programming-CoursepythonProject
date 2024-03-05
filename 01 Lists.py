# Lists ordered, mutable, allows duplicate elements

myList = ["banana", "cherry", "apple"]
print(myList)

myList2 = list()
print(myList2)

myList2 = [5, True, "apple", "apple"]
print(myList2)

item = myList[0]
print(item)

item = myList[-1]
print(item)

for i in myList:
    print(i)

if "banana" in myList:
    print("yes")
else:
    print("no")

print(len(myList))

myList.append("lemon")
print(myList)

myList.insert(1, "blueberry")
print(myList)

item = myList.pop()
print(item)
print(myList)

item = myList.remove("cherry")
print(item)
print(myList)

item = myList.reverse()
print(item)
print(myList)

#myList.sort()
new_list = sorted(myList)
print(new_list)

myList = [0] * 5
print(myList)

myList2 = [1, 2, 3, 4, 5]
new_list = myList + myList2
print(new_list)

a = myList2[1:3]
print(a)

a = myList2[::2]
print(a)

list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
list_cpy.append("lemon")
print(list_org)
print(list_cpy)

list_cpy = list(list_org)
print(list_org)
print(list_cpy)

a = [1, 2, 3, 4, 5, 6]
b = [i*i for i in a]
print(myList)
print(b)
