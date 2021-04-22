# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:16:27 2021

@author: guanglan
Some are from Prof. Pinsky
"""
# Mutability
x_int = 5
y_int = 5
print(id(x_int), id(y_int))
x_int = 10
print(id(x_int), id(y_int))

x_float = 9.5
y_float = 9.5
print(id(x_float), id(y_float))
x_float = 10.5
print(id(x_float), id(y_float))

x_str = "Boston"
y_str = "Boston"
z_str = "boston"
print(id(x_str), id(y_str), id(z_str))
x_str[0] = "b"  # Invalid: String is immutable

x_tuple = (1, 2, 3, 3)
x_tuple[0] = 10  # Invalid: Tuple is immutable
y_tuple = (1, 2, 3, 3)  # need a new object
print(id(x_tuple), id(y_tuple))

x_tuple = ([1, 2], 3)
print(x_tuple, id(x_tuple))
x_tuple[0][0] = 4
x_tuple[0][1] = 5
print(x_tuple, id(x_tuple))

x_list = [1, 2, 3]
print(id(x_list))
x_list[0] = 'cat'   # list is mutable
print(x_list, id(x_list))   # still the same object
last_item = x_list.pop(-1)
print(x_list, id(x_list))

x_set = {1, 2, 3, 3}
print(x_set, id(x_set))
random_item = x_set.pop()  # set is mutable
print(x_set, id(x_set))

x_dict = {"Alice": 88, "Bob": 90}
y_dict = {"Alice": 88, "Bob": 90}
print(id(x_dict), id(y_dict))
x_dict["Alice"] = 100  # dictionary is mutable
print(x_dict, id(x_dict))
an_item = x_dict.pop("Bob")
print(x_dict, id(x_dict))

# constructors
x_str = 'orange'
print(x_str, type(x_str))
y_str = str('orange')
print(y_str, type(y_str))

x_list = [1, 4.5, "Python"]
print(x_list, type(x_list))
y_list = list((1, 4.5, "Python"))  # note the double breackets
print(y_list, type(y_list))

x_tuple = (1, 4.5, 'Python')
print(x_tuple, type(x_tuple))
y_tuple = tuple((1, 4.5, "Python"))  # note the double breackets
print(y_tuple, type(y_tuple))

x_set = {1, 4.5, 1, 4.5}
print(x_set, type(x_set))
y_set = set({1, 4.5, 1, 4.5})  # note the double breackets
print(y_set, type(y_set))

x_dict = {'Alice': 100, 'Bob': 88}
print(x_dict, type(x_dict))
y_dict = dict({'Alice': 100, 'Bob': 88})  # note the double breackets
print(y_dict, type(y_dict))

# integer conversion
x_int = 30
x_bin = bin(x_int)  # base 2
x_oct = oct(x_int)  # base 8
x_hex = hex(x_int)  # base 16
print(x_bin, x_oct, x_hex)

# int and float are objects with methods
x_int = 7
x_bits = x_int.bit_length()

y_float = 0.75
y_ratio = y_float.as_integer_ratio()

# divmod()
x = 7 / 2
x_floor = 7 // 2
x_remainder = 7 % 2
print(x, x_floor, x_remainder)
x_tuple = divmod(7, 2)
print(x_tuple)

z = 7.0 / 2.2
z_floor = 7.0 // 2.2
z_remainder = 7.0 % 2.2
print(z, z_floor, z_remainder)
z_tuple = divmod(7.0, 2.2)
print(z_tuple)

# indexing and iteration
x_str = 'Python'
print(x_str[0], x_str.index('P'))

VOWELS = 'aeoiuy '
x_list = ['a', 'p', 'p', 'l', 'e']
i = 0
while i < len(x_list):
    e = x_list[i]
    if e in VOWELS:
        print(e, i)
    i = i + 1

print(list(range(len(x_list))))  # to display
for i in range(len(x_list)):
    e = x_list[i]
    if e in VOWELS:
        print(e, i)

print(list(enumerate(x_list)))  # to display
for i, e in enumerate(x_list):
    if x_list[i] in VOWELS:
        print(e, i)

# range() example
# Calculate the sum of first n positive even integers
in_str = input("Enter a positive integer:")
n = int(in_str)
x_list = list(range(2, 2*n+1, 2))
s = 0
for e in x_list:
    s += e
print(n, s)

# Exercise using range()
# construct a list of every 7-th integer from 1 to 50

step = 7
x_list = list(range(1, 51, step))
print(x_list)

# sum up every 7-th integer from 1 to 50
s = 0
for e in x_list:
    s += e
print(s)

# alternatively
print(sum(x_list))


