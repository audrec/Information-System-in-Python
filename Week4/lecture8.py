# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 00:53:59 2021

@author: guanglan
"""
# sets
x_set = set()
x_set = set('apple')
y_set = {'apple'}
z_set = set(range(5))

# An empty set is falsy
x_set = set()
bool(x_set)
x_set or True
x_set and True

# elements must be immutable objects
x_set = {1, 'apple', (2.3, 'cat')}
y_set = {1, 'apple', [2.3, 'cat']}  # TypeError
y_set = {1, 'apple', {2.3: 'cat'}}  # TypeError

# sets are unordered
{1, 2, 3} == set([2, 1, 3])

# set union
x_set = {'apple', 'orange', 'melon'}
y_set = {'apple', 'kiwi', 'strawberry'}
y_list = ['apple', 'kiwi', 'strawberry']
z_set = {"grape", "melon", "kiwi"}
u1 = x_set.union(y_set)
u2 = x_set.union(y_list)
u3 = x_set | y_set
# u4 = x_set | y_list  # TypeError
u5 = x_set.union(y_set, z_set)
u6 = x_set | y_set | z_set
print(u1, u2, u3, u5, u6, sep="\n")

# set intersection
s1 = x_set.intersection(y_set)
s2 = x_set.intersection(y_list)
s3 = x_set & y_set
# s4 = x_set & y_list  # TypeError
s5 = x_set.intersection(y_set, z_set)
s6 = x_set & y_set & z_set
print(s1, s2, s3, s5, s6)

# set difference
d1 = x_set.difference(y_set)
d2 = x_set.difference(y_list)
d3 = x_set - y_set
# d4 = x_set - y_list  # TypeError
d5 = y_set.difference(x_set)
d6 = y_set - x_set
d7 = x_set.difference(y_set, z_set)
d8 = x_set - y_set - z_set
print(d1, d2, d3, d5, d6, d7, d8, sep="\n")

# set symmetric difference
sd1 = x_set.symmetric_difference(y_set)
sd2 = x_set.symmetric_difference(y_list)
sd3 = x_set ^ y_set
sd4 = x_set ^ y_set ^ z_set
sd5 = x_set.symmetric_difference(y_set, z_set)  # invalid
print(sd1, sd2, sd3, sd4, sep="\n")

# check if two collections have anyting in common
x_set.isdisjoint(y_set)
x_set.isdisjoint(y_list)

# check if a set is a subset of another
x_set.issubset(y_set)
x_set.issubset(y_list)
x_set.issubset(x_set)  # a set is a subset of itself
x_set <= y_set
x_set <= x_set
x_set.issubset(u1)
x_set <= u1

# a proper subset is same as a subset, but two sets cannot be identical
x_set < x_set
x_set < u1

# superset
x_set.issuperset(y_set)
x_set.issuperset(y_list)
x_set.issuperset(x_set)  # a set is a superset of itself
x_set >= y_set
u1.issuperset(x_set)
u1 >= x_set

# proper superset
u1 > x_set
x_set > x_set

# sets are mutable
x_set = {'apple', 'orange', 'melon'}
print(x_set, id(x_set))
x_set.add('kiwi')
x_set.add('melon')
print(x_set, id(x_set))

x_set = {'apple', 'orange', 'melon'}
y_set = {'apple', 'kiwi', 'strawberry'}
x_set.update(y_set)

x_set = {'apple', 'orange', 'melon'}
y_set = {'apple', 'kiwi', 'strawberry'}
x_set |= y_set

# set comprehension
# the list includes duplicates and names with only a single letter
# We like to remove duplicates and single letter names, and capitalize all
names = ['Arnold', 'BILL', 'alice', 'arnold', 'MARY', 'J', 'BIll']
formatted = {x.capitalize() for x in names if len(x) > 1}
print(formatted)

char_dict = {'A': 4, 'z': 2, 'D': 8, 'a': 5, 'Z': 10}
# Count the number of occurrence of the letters regardless of their case
new_dict = {k.lower(): char_dict.get(k.lower(), 0) +
            char_dict.get(k.upper(), 0) for k in char_dict.keys()}
print(new_dict)

# frozen set
x_set = {1, 2}
frozen_x = frozenset(x_set)
frozen_x.add(3)  # invalid
x_dict = {x_set: "Apple"}
x_dict = {frozen_x: "Apple"}
print(x_dict)

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

# sort dictionary based on keys
x_dict = dict(f1="Apple", f3="Kiwi", f2="Orange")
print(sorted(x_dict))


# sort dictionary based on values
def first_index(x):
    ''''get the data at index 1 '''
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


# function
def multi_div(a, b):
    '''multiply and divide two numbers '''
    x, y = a*b, a/b
    return x, y


def multi_div1(a, b):
    '''multiply and divide two numbers and check for exception '''
    x = a*b
    try:
        y = a/b
    except:
        y = "cannot divide"

    return x, y


print(multi_div)
print(multi_div.__doc__)
multi_div(5, 1)
multi_div(5, 0)

print(multi_div1)
print(multi_div1.__doc__)
multi_div1(5, 0)

