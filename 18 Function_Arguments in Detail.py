def print_name(name): # parameter
    print(name)


def foo(a, b, c, d=4): # default argument must be last
    print(a, b, c, d)


def foo1(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


def foo2(a, b, *, c, d):
    print(a, b, c, d)


def foo3(*args, a, b, c, d):
    print(a, b, c, d)


def foo4(*args, last):
    for arg in args:
        print(arg)
    print(last)


def foo5():
    global number
    x = number
    number = 100
    print('Global variable number=', x)
    number = 3
    print('Global variable changed: number=', number)


def foo6(a, b, c):
    print(a, b, c)


def foo7(a_list):
    a_list.append(4)


print_name('Hello') # argument

print("\nFoo ---------------------")
foo(c=1, b=2, a=3) # keywordargument kwargs, order not important

foo(1, b=2, c=3) # keywordargument kwargs, order important

foo(1, b=2, c=3, d=7) # keywordargument kwargs, order important

print("\nFoo1 ---------------------")
foo1(1, 2, 3, 4, 5, six=6, seven=7)
foo1(1, 2, 3, 4)

print("\nFoo2 ---------------------")
foo2(1, 2, c=3, d=4)

print("\nFoo3 ---------------------")
foo3(a=1, b=2, c=3, d=4)

print("\nFoo4 ---------------------")
foo4(1, 2, 3, last=100)

print("\nFoo5 ---------------------")
number = 0
foo5()

print("\nFoo6 ---------------------")
my_list = [0, 1, 2]
foo6(*my_list)
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo6(**my_dict)


print("\nFoo7 ---------------------")
my_list = [1, 2, 3]
foo7(my_list)
print(my_list)
