# Tuple: ordered, immutable, allows duplicate elements
mytuple = ("max", 28, "Boston")
print(type(mytuple))
print(mytuple)

mytuple = tuple(["max", 28, "Boston"])
print(mytuple)

item = mytuple[1]
print(item)

for x in mytuple:
    print(x)
if "Max" in mytuple:
    print("Yes")
else:
    print("No")

mytuple = ('a', 'p', 'p', 'l', 'e')
print(len(mytuple))
print(mytuple.count("p"))

mylist = list(mytuple)
print(mylist)

mytuple = tuple(mylist)
print(mytuple)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
b = a[:5]
print(b)
b = a[2:]
print(b)
b = a[::2]
print(b)

mytuple = ("max", 28, "Boston")
name, age, city = mytuple
print(name)
print(age)
print(city)

mytuple = (1, 2, 3, 4)
i1, * i2, i3 = mytuple
print(i1)
print(i3)
print(i2)


#immutable
mytuple[0] = "Tim"
