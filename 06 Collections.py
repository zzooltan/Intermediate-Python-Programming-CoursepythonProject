# Collections: Counter, namedtuple, OrderDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

# Counter
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

#namedtuples
Point = namedtuple('point','x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# OrederedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
ordered_dict['a'] = 1
print(ordered_dict)

# defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['b'])

# deque
d = deque()
d.append(1)
d.append(2)
d.append(4)
d.appendleft(3)
d.pop()
print(d)
d.popleft()
print(d)
d.extend([5, 6, 7])
print(d)
d.extendleft([8, 9])
print(d)
d.rotate(1) #rotate right, -1 rotate left
print(d)
d.clear()
print(d)