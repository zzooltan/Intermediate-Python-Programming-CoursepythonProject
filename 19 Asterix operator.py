#Multiplication
print('\nMultiplication------------------------')
result = 5 * 7
print(result)

print('\nPower operation------------------------')
result = 2 ** 4
print(result)

print('\nList multiplication -------------------')
zeros = [0, 2] * 7
print(zeros)

print('\nTuple multiplication ------------------')
zeros = (0, 29) * 7
print(zeros)

print('\nString multiplication -----------------')
zeros = "hello world " * 7
print(zeros)


def foo1(a, b, *args, **kwargs):
    print(a)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)


def foo2(a, b, *, c):
    print(a, b, c)

def foo3(a, b, c):
    print(a, b, c)


print('\nfoo1(a, b, *args, **kwargs) -----------------------')
foo1(1, 2,  3, 4, 5, six=6, seven=7)

print('\nfoo2(a, b, *, c) -----------------------')
foo2(1, 2, c=3)

print('\nfoo3(*my_list) - list unpacking 1 -------------------')
my_list = [0, 1, 2]
foo3(*my_list)

print('\nfoo3(*my_tuple) - tuple unpacking -------------------')
my_tuple = (3, 4, 5)
foo3(*my_tuple)

print('\nfoo3(*my_dict) - dictionary unpacking -------------------')
my_dict = {'a': 6, 'b': 7, 'c': 8}
foo3(**my_dict)

print('\n*beginning, last = numbers - list unpacking 2------------')
numbers = [1, 2, 3, 4, 5, 6]
*beginning, last = numbers
print(beginning)
print(last)


print('\nbeginning, *last = numbers - list unpacking 3------------')
numbers = [1, 2, 3, 4, 5, 6]
beginning, *last = numbers
print(beginning)
print(last)


print('\nbeginning, *middle, last = numbers - list unpacking 4------------')
numbers = [1, 2, 3, 4, 5, 6]
beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

print('\nnew_list =[*my_tuple, *my_list] - merging 1------------')
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
new_list =[*my_tuple, *my_list]

print('\nnew_list =[*my_tuple, *my_set] - merging 2------------')
my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
new_list =[*my_tuple, *my_set]

print('\nmy_dicta = {**my_dicta, **my_dictb} - merging 3------------')
my_dicta = {'a': 1, 'b': 2, 'c': 3}
my_dictb = {'d': 4, 'e': 5, 'f': 6}
my_dict = {**my_dicta, **my_dictb}
print(my_dict)