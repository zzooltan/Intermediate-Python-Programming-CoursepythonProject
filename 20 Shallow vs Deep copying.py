import copy
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

print('\nshallow copy an integer')
org = 5
cpy = org
print('org=', org)
print('cpy=', cpy)

print('\nshallow copy a list')
org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print('org=', org)
print('cpy=', cpy)

print('\nFull copy of List')
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
cpy[0] = -10
print('org=', org)
print('cpy=', cpy)

print('\nFull copy of slicing of a List')
org = [0, 1, 2, 3, 4]
cpy = org[:]
cpy[0] = -10
print('org=', org)
print('cpy=', cpy)


print('\nShallow copy of nested List')
org = [[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print('org=', org)
print('cpy=', cpy)

print('\nDeep copy of nested List')
org = [[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print('org=', org)
print('cpy=', cpy)


print('\nClass copy')
p1 = person('Alex', 27)
p2 =p1
p2.age = 28
print(p2.age)
print(p1.age)


print('\n Shallow Class copy')
p1 = person('Alex', 27)
p2 = copy.copy(p1)
p2.age = 28
print(p2.age)
print(p1.age)


print('\n Shallow Multilevel Class copy')
p1 = person('Alex', 55)
p2 = person('Joe', 27)
company = Company(p1, p2)
company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)


print('\n Deep Multilevel Class copy')
p1 = person('Alex', 55)
p2 = person('Joe', 27)
company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)