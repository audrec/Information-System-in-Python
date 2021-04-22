# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:15:21 2021

@author: guanglan

"""
# if-elif-else
a, b, c = 4, 7, 6
if a < b and b < c:
    print('data are in ascending order')
elif a > b and b > c:
    print('data are in descending order')
else:
    print('data are not in order')

# for loop
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for i, e in enumerate(fibonacci):
    print("index: ", i, " number: ", e)
else:
    print("Loop done!")

# break
for i, e in enumerate(fibonacci):
    if i == 5:
        break

    print("index: ", i, " number: ", e)
else:
    print("Loop done!")

towns = ["Brookline", "Arlington", "Newton", "Westen"]
# hometown = "Belmont"
hometown = "Newton"
for place in towns:
    if place == hometown:
        print(f"Found {hometown} in the list!")
        break
else:
    print("Not able to find {hometown} in the list.")

if hometown in towns:
    print(hometown, 'found in list.')
else:
    print(hometown, 'not found in list.')

# continue
for i, e in enumerate(fibonacci):
    if i == 5:
        continue

    print("index: ", i, " number: ", e)
else:
    print("Loop done!")

# pass
for i, e in enumerate(fibonacci):
    if e % 2 == 0:
        pass  # placeholder

    print("index: ", i, " number: ", e)

# compute product of the Fibonacci numbers (exclude the first one)
n = 5
f = [0, 1]
product = 1
i = 2
while i < n:
    f.append(f[i-1] + f[i-2])
    product *= f[i]
    i += 1

print("First five Fabonacci nubmers: ", f)
print("Their product: ", product)

# strings
x_str = 'orange'
y_str = "Apple"
z_str = """orange
Apple"""

# +, *, in, not in
x_str + y_str
x_str * 2
"e" in x_str
"Ap" in x_str
"Ap" not in x_str

# Iteration
VOWELS = 'aeiouy'
for e in x_str:
    if e in VOWELS:
        print(e)

for i, e in enumerate(x_str):
    if e in VOWELS:
        print(e)

# built-in string functions
v_str = str(3+5)
print(len(z_str))
ord(' ')
ord('a')
ord('A')
chr(97)

# indexing and slicing
x_str = "New York"
print(len(x_str))
print(x_str[4:7])  # half-open range, index 7 is not included
print(x_str[11])  # out of range index; error
print(x_str[9:11])  # out of range; no error
x_str[:2]
x_str[-2:]
x_str[::2]
x_str[1::2]
x_str[-100:5]  # out-of-bound slicing
x_str[3:100]   # out-of-bound slicing
x_str[50:100]  # out-of-bound slicing
x_str[::-1]

# strings are immutable, how to modify strings
x_str = "Applepie"
print(x_str, id(x_str))
y_str = "Apple" + "pie"
print(y_str, id(y_str))
x_str = x_str[:5] + 'P' + x_str[-2:]
print(x_str, id(x_str))
x_str = x_str.replace("e", "X")
print(x_str, id(x_str))

# Built-in string methods
# character classification
x_str = "BostonMarathon2021"
x_str.isalnum()
x_str.isalpha()
x_str.isdigit()
x_str = "BostonMarathon"
x_str.isalnum()
x_str.isalpha()
x_str.isdigit()
x_str = "15"
x_str.isalnum()
x_str.isalpha()
x_str.isdigit()

# find substring
x_str = "Applepie is my favorite"
x_str.count('pi', 0, 8)
x_str.endswith('te')
x_str.startswith('is', 9)
x_str.find('PIE')
x_str.find('e')
x_str.find('e', x_str.find('e')+1)  # nesting of methods
x_str.index('e')
x_str.rindex('e')
x_str.index('E')   # invalid

# case conversion
x_str = "applepiE is my favorite"
x_str.capitalize()
x_str.lower()
x_str.swapcase()
x_str.title()
x_str.upper()
x_str.upper().find("PIE")  # chaining of methods

# string -> list; list -> string
z_str = """Tom likes orange
Apple"""
z_str.split()
z_str.split(sep='\n')
z_str.split(maxsplit=2)
z_str.rsplit(maxsplit=2)
z_str.splitlines()

z_list = ["Tom", "likes", "orange", "apple"]
z1 = " ".join(z_list)
z2 = ":".join(z_list)
z3 = ":".join(z_list[-1])
print(z1, z2, z3, sep="\n")

z_list = ["Tom", "likes", "orange", "apple", 24]
z1 = " ".join(z_list)

z_list = ["Tom", "likes", "orange123", "apple$$"]
v_list = list(filter(str.isalnum, z_list))
v_str = " ".join(v_list)
print(v_str)

# Compare strings
towns = ["Brookline", "Arlington", "Newton", "newton"]
hometown = "Newton"

for place in towns:
    print(f"comparing {place} with {hometown}: {place == hometown}")

# Case insensitive comparison
for place in towns:
    print(f"comparing {place} with {hometown}: \
          {place.lower() == hometown.lower()}")

# Comparison according to a lexicographical order
for place in towns:
    if place < hometown:
        print("%s comes before %s" % (place, hometown))
    elif place > hometown:
        print("%s comes after %s" % (place, hometown))
    else:
        print("%s is similar to %s" % (place, hometown))


# check ssn format
x_str = '123-45-6789'
y_list = x_str.split("-")
valid = False
if len(y_list) == 3:
    if (y_list[0].isdigit() is True and len(y_list[0]) == 3) and \
        (y_list[1].isdigit() is True and len(y_list[1]) == 2) and \
            (y_list[2].isdigit() is True and len(y_list[2]) == 4):
        valid = True

if valid is True:
    print(x_str, 'is a valid ssn')
else:
    print(x_str, 'is not a valid ssn')


# Exercise
a = [1, 2, 3, 4, 5]
while a:
    if len(a) < 3:
        break
    print(a.pop())
else:
    print('Done.')

a = [1, 2, 3, 4, 5]
while a:
    if len(a) < 3:
        continue
    print(a.pop())
else:
    print('Done.')


x_str = 'Boston'
y_str = 'Univ.'
z_str = 2 * (x_str + y_str)
print(z_str[-100:2])
print('tonU' in z_str)
print(z_str.index('tonU'))
print(z_str.index('tonu'))  # invalid
print(z_str.find('tonU'))
print(z_str.find('tonu'))
print(z_str.rindex('v.'))
