# lambda arguments: expression
from functools import reduce
#map(func, seq)

add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y: x * y
print(mult(6, 7))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print(points2D)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D)
print(points2D_sorted)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))

c = [x * 2 for x in a]
print(c)

# filter(func, seq) return true or false
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a) #return even number
print(list(b))

#reduce(func, seq)
a = [1, 2, 3, 4, 5, 6]
product_a = reduce(lambda x, y: x * y, a)
print(product_a)
