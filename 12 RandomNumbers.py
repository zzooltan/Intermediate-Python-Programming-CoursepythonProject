
import random
import secrets
import numpy as np

a = random.random()
print(a)

a = random.randint(1, 10)
print(a)

a = random.randrange(1, 10) # never be 10
print(a)

a = random.normalvariate(0, 1)
print(a)

mylist = list("ABCDEFGH")
a = random.choice(mylist)
print(a)

mylist = list("ABCDEFGH")
a = random.sample(mylist, 3) # not repeat an element
print(a)

mylist = list("ABCDEFGH")
a = random.choices(mylist, k=3) # repeat element
print(a)


mylist = list("ABCDEFGH")
random.shuffle(mylist)
print(mylist)
# --------------------------------------

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
print("\n")
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
# --------------------------------------

a = secrets.randbelow(10) # 10 not included
print(a)

a = secrets.randbits(4) # from b0000 - b1111 in decimal
print(a)

mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)
# --------------------------------------

a = np.random.rand(3) # 3 random number
print(a)

a = np.random.rand(3, 3) #give 3 x 3 array random number
print(a)

a = np.random.randint(0, 10, 4) # 4 peaces random number
print(a)

a = np.random.randint(0, 10, (4, 2)) # 4 x 2 array random number
print(a)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)
# --------------------------------------
np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(2)
print(np.random.rand(3, 3))




