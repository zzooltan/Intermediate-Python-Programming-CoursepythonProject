import json
from json import JSONEncoder

# convert to json
person = {"firstName": "John", "age": "30", "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# json to file
with open('person.json', 'w') as file:
    json.dump(person, file, indent= 4)

# convert from json
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
# ----------------------------------------------


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type is not json serializable")


user = User("Max", 27)
userJson = json.dumps(user, default=encode_user, indent=4)
print(userJson)
# -----------------------------------------------------


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

# from python to json
user = User("John", 30)
userJson = UserEncoder().encode(user)
print(userJson)

# from json to python
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct["age"])
    return dct


user = json.loads(userJson, object_hook=decode_user)
print(type(user))
print(user.name, user.age)
