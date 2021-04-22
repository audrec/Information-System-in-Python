# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:32:11 2021

@author: guanglan
Some examples are from Prof. Pinksky
"""
# The comma is the operator that creates the tuple
x_tuple = ()
y_tuple = tuple()
print(y_tuple == x_tuple)

y_tuple = (1, 2, 3)
z_tuple = 1, 2, 3
print(y_tuple == z_tuple)

x_tuple = (1)
y_tuple = (1,)
print(x_tuple, y_tuple)

# Tuple is ordered
(1, 2, 3) == (2, 1, 3)

# indexing and slicing
print(x_tuple[0], x_tuple[-1])
print(x_tuple[-2:])
print(x_tuple[::-1])  # reverse a list
print(x_tuple[10])  # out of range index; error
print(x_tuple[9:11])  # out of range; no error
print(x_tuple[-100:5])  # out-of-bound slicing

# Tuples are immutable
x_tuple = (1, 2, 3)
x_tuple[0] = 4  # TypeError
del x_tuple[0]  # TypeError

# operators +, *, in, not in
y_tuple = (4, 5, 6)
z_tuple = x_tuple + y_tuple
print(z_tuple, id(x_tuple), id(y_tuple), id(z_tuple))

y_tuple = 3*x_tuple
print(x_tuple, y_tuple)

print(1 in x_tuple)
print(4 not in x_tuple)

# len(), min(), max(), sum()
len(x_tuple)
min(x_tuple)
max(x_tuple)
sum(x_tuple)

# search in a tuple
x_tuple = ("Apple", "Orange", "Orange")
x_tuple.index('Orange')
x_tuple.index('kiwi')  # ValueError
x_tuple.count("Orange")
x_tuple.count('kiwi')

# iterate through a tuple
x_tuple = tuple('MET CS521 Information Structure with Python')
VOWELS = 'aeoiuyAEOIUY'
for e in x_tuple:
    if e in VOWELS:
        print(e, end="")

for i, e in enumerate(x_tuple):
    if e in VOWELS:
        print(e, i)

#  Dictionaries are mutable
x_dict = dict()  # empty dict
y_dict = {}  # empty dict

x_dict = {"Boston": "Patriots", "New York": "Gaints"}
print(x_dict, id(x_dict))
x_dict["Dallas"] = "Cowboys"
x_dict['Boston'] = "something else"
print(x_dict, id(x_dict))

# anotehr way to create a dict - using a list of tuples
y_dict = dict([("Boston", "Patriots"), ("New York", "Gaints")])
print(y_dict)

# duplicate keys are not allowed
y_dict = dict([("Boston", "Patriots"), ("Boston", "Gaints")])
print(y_dict)

# Tuples can be keys
y_dict = {("Boston", "MA"): "Patriots", ("New York", "NY"): "Gaints"}
print(y_dict)

# lists cannot be keys
y_dict = {["Boston", "MA"]: "Patriots", ["New York", "NY"]: "Gaints"}

# construct using zip()
city_list = ["Boston", "Dallas", "New York"]
team_list = ["Patriots", "Cowboys", "Gaints"]
football_list = list(zip(city_list, team_list))
football_dict = dict(zip(city_list, team_list))
print(football_list, football_dict)

# two lists of different lengths
city_list = ["Boston", "Dallas", "New York", "Chicago"]
team_list = ["Patriots", "Cowboys", "Gaints"]
football_list = list(zip(city_list, team_list))
football_dict = dict(zip(city_list, team_list))
print(football_list, football_dict)

# using dict.fromkeys()
key_list = list('aeiouy')
counter_dict = dict.fromkeys(key_list, 0)
print(counter_dict)

# Retrieve a value
y_dict = dict([("Boston", "Patriots"), ("New York", "Gaints")])
Boston_team = y_dict["Boston"]
Dallas_team = y_dict["Dallas"]   # When the key does not exist
# To avoid error, use short-circuit evaluation
'Dallas' in y_dict and y_dict["Dallas"]
'Boston' in y_dict and y_dict["Boston"]

print(x_dict.get("Boston"))
print(x_dict.get("boston"))
print(x_dict.get("boston", "Does not exist!"))

x_dict.setdefault("Boston")
x_dict.setdefault("boston")
x_dict.setdefault("Pittsburgh", "Steelers")

key_list = list(x_dict.keys())
value_list = list(x_dict.values())
item_list = list(x_dict.items())

# remove specified keys
x_dict = {"Boston": "Patriots", "New York": "Gaints", "Dallas": "Cowboys"}
del x_dict["Boston"]
del x_dict["boston"]  # Error when the key does not exist

team = x_dict.pop("Boston")
print(x_dict, team)
team = x_dict.pop("Boston")  # error when the key does not exist
team = x_dict.pop("Boston", "Does not exist!")
print(x_dict, team)

x_dict = {"Boston": "Patriots", "New York": "Gaints", "Dallas": "Cowboys"}
del_list = ["boston", "Boston", "New York"]
[x_dict.pop(k, -1) for k in del_list]
print(x_dict)

x_dict.popitem()
x_dict.popitem()  # error when try to apply on an empty dict

# for iteration
x_dict = dict([(1, "Patriots"), (2, "Gaints"),
               (3, "Cowboys"), (4, "Steelers")])
for k in x_dict:
    if k % 2 == 0:
        print(k, x_dict[k])

for k, v in x_dict.items():
    if k % 2 == 0:
        print(k, v)

# dict comprehension. General format:
# new_dict = {key:value for (key,value) in old_dict.items()}
z_dict = {k: v for k, v in x_dict.items() if k % 2 == 0}
print(z_dict)

# update a dictionary
x_dict = dict(f1="Apple", f2="Orange", f3="Kiwi")
y_dict = {"f2": "Melon", "f5": "Kiwi"}
x_dict.update(y_dict)
print(x_dict)

x_dict = dict(f1="Apple", f2="Orange", f3="Kiwi")
x_dict.update(f2="Melon", f5="Kiwi")
print(x_dict)

# access data in sub-list or sub-dict
person = dict()
person['name'] = 'John'
person['age'] = 40
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Inka', 'cat': 'Smart'}
print(f"{person['name']} has {len(person['children'])} children.")
print(f"He named the first child {person['children'][0]}.")
print(f"His dog's name is {person['pets']['dog']}.")

# sort data
x_list = ['Ralph', 'Betty', 'Alice']
print(id(x_list))
x_list.sort()
print(x_list, id(x_list))

x_list = ['Ralph', 'betty', 'Alice']
print(id(x_list))
y_list = sorted(x_list, reverse=True)  # sort decendingly
print(y_list, id(y_list))
y_list = sorted(x_list, reverse=True, key=str.lower)  # case insensitive
print(y_list, id(y_list))

x_dict = dict(f1="Apple", f3="Kiwi", f2="Orange")
print(sorted(x_dict))


def first_index(x):
    return x[1]


x_dict = dict(f3="Kiwi", f2="Orange", f1="Apple")
y_dict = dict(sorted(x_dict.items(), key=first_index))
print(y_dict)

y_list = sorted(x_dict.items(), key=lambda x: x[1])
print(y_list, dict(y_list))

# count the nubmers of vowels in each value
VOWELS = 'aeiouy'
x_dict = {"Boston": "Patriots", "New York": "Gaints", "Dallas": "Cowboys"}
count_dict = dict.fromkeys(x_dict.keys(), 0)
for k, v in x_dict.items():
    for e in v.lower():
        if e in VOWELS:
            count_dict[k] += 1

count_dict = dict.fromkeys(x_dict.keys(), 0)
for k, v in x_dict.items():
    for e in VOWELS:
        count_dict[k] += v.lower().count(e)


count_dict = {k: len(list(filter(lambda x: (x in VOWELS), v.lower())))
              for k, v in x_dict.items()}


# Exercises
# 1. use zip() to construct the following list
# x_list=[("tiger", ("cat","forest")),
#         ("lion", ("cat", "plains")),
#         ("salmon",("fish","water"))]


# 2. Show two ways to add the item ("eagle", ("bird“, “mountain”)
# to the above x dict


# 3. Use comprehension to construct y_dict from x_dict containg value "cat":
x_dict = {"tiger": "cat", "lion": "cat", "salmon": "fish"}


