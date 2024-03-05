# Strings: ordered, immutable, text representation
from timeit import default_timer as timer

my_string = "Hello word"
print(my_string)

my_string = 'I\'m a programmer'
print(my_string)

my_string = """Hello 
world"""
print(my_string)

char = my_string[0]
print(char)

substring = my_string[1:5]
print(substring)

greeting = "hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

for i in greeting:
    print(i)

if 'e' in greeting:
    print("yes")
else:
    print("No")

my_string = '    Hello World    '
print(my_string)
my_string = my_string.strip()
print(my_string)

print(my_string.upper()+ " "+my_string.lower())
print(my_string.startswith("H"))

print(my_string.find("lo"))
print(my_string.find("as"))

print(my_string.count("o"))

print(my_string.replace('World', 'universe'))

my_string = 'How are you doing'
my_list = my_string.split()
print(my_list)

new_string = ' '.join(my_list)
print(new_string)

my_list = ['a'] * 6
print(my_list)

start = timer()
my_string = ''
for i in my_list:
    my_string += i
print(my_string)
stop = timer()
print(stop-start)

start = timer()
my_string = ''.join(my_list)
print(my_string)
stop = timer()
print(stop-start)

# foramtting string

var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 3
my_string = "the variable is %d" % var
print(my_string)

var = 3.12345
my_string = "the variable is %.2f" % var
print(my_string)

var = 3.12345
var2 = 6
my_string = "the variable is {:.2f} and {:.2f}".format(var,var2)
print(my_string)

my_string = f"the variable is {var*2} and {var2}"
print(my_string)