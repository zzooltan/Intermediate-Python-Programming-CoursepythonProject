# Dictionary: key-values pairs, Unordered, Mutable
from builtins import print

mydict = {"name": "Max", "age": 28, "city": "New York"}

print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

value = mydict["name"]
print(value)

mydict["email"] = "max@xyz.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem() #delete last element
print(mydict)

if "city" in mydict:
    print(mydict["city"])

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("error")

mydict = {"name": "Max", "age": 28, "city": "New York"}

for key in mydict:
    print(key)

for v in mydict.values():
    print(v)

for key, value in mydict.items():
    print(key, value)
# copying
mydic_cpy = mydict
print(mydic_cpy)
mydic_cpy["email"] = "max&xmz.com"
print(mydict)
print(mydic_cpy)

mydict = {"name": "Max", "age": 28, "city": "New York"}
mydic_cpy = mydict.copy()
print(mydic_cpy)
mydic_cpy["email"] = "max&xmz.com"
print(mydict)
print(mydic_cpy)

# merging
mydict = {"name": "Max", "age": 28, "email": "max&xmz.com","city": "New York"}
mydict2 = dict(name="Mary", age=27, city="Boston")

mydict.update(mydict2)
print(mydict)

mydict = {3: 9, 6: 36, 9: 81}
print(mydict)
print(mydict[3])

mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)

