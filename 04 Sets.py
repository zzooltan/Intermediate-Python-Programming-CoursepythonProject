# Sets: unordered, mutable, no duplicates

myset = {1, 2, 3}
print(type(myset))
print(myset)

myset = set([1, 2, 3])
print(myset)

myset = set("hello")
print(myset)

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset.remove(3)
print(myset)

myset.discard(3) # nem dob hibát, ha nincs olyan elem
print(myset)

myset.pop()
print(myset)
myset.clear()
print(myset)

myset = set([1, 2, 3])

for i in myset:
    print(i)

if 1 in myset:
    print("yes")
else:
    print("no")

# Union and intersection

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)
i = odds.intersection(primes)
print(i)
i = evens.intersection(primes)
print(i)

# Difference
seta = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setb = {1, 2, 3, 10, 11, 12}

d = seta.difference(setb)
print(d)

d = seta.symmetric_difference(setb)
print(d)

seta.update(setb)
print(seta)

seta = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setb = {1, 2, 3, 10, 11, 12}
seta.intersection_update(setb)
print(seta)

seta = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setb = {1, 2, 3, 10, 11, 12}
seta.difference_update(setb)
print(seta)

seta = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setb = {1, 2, 3, 10, 11, 12}
seta.symmetric_difference_update(setb)
print(seta)

seta = {1, 2, 3, 4, 5, 6}
setb = {1, 2, 3}
setc = {7, 8}
print(seta.issubset(setb))
print(setb.issubset(seta))
print(setb.issuperset(seta))
print(seta.issuperset(setb))
print(seta.isdisjoint(setb))
print(seta.isdisjoint(setc))

setb = seta.copy()
print(setb)
print(seta)

#frosen set, unmutable version if norma set

a = frozenset([1, 2, 3, 4, 5])
print(a)
a.add(8) # make error, couse unmutable

print(a)


