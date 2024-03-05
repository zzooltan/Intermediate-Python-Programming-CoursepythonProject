import sys


def mygenerator():
    yield 3
    yield 2
    yield 1


def countdown(num):
    print('Staring')
    while num > 0:
        yield num
        num -= 1


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


def fibonacci(limit):
    # 0 1 next is 0+1 next is 1+2
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


g = mygenerator()
print(g)
# ----------------------------
print('-----------------------')
g = mygenerator()
for i in g:
    print(i)
# ----------------------------
print('-----------------------')
g = mygenerator()
value = next(g)
print(value)
value = next(g)
print(value)
# -----------------------------
print('-----------------------')
g = mygenerator()
print(sorted(g))
# ------------------------------
print('-----------------------')
cd = countdown(5)
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
# ------------------------------
print('-----------------------')
print(firstn(10))
print(sum(firstn(10)))
# ------------------------------
print('-----------------------')
print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))
# ------------------------------
print('-----------------------')
fib = fibonacci(30)
for i in fib:
    print(i)
# ------------------------------
print('-----------------------')
mygenerator = (i for i in range(1000000) if i % 2 == 0) # generator object
print(sys.getsizeof(mygenerator))
#for i in mygenerator:
#    print(i)
print('-----------------------')
mylist = [i for i in range(1000000) if i % 2 == 0] #with list
print(sys.getsizeof(mylist))
#print(mylist)
