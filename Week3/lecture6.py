# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:32:11 2021

@author: guanglan
"""
# List is ordered
[1, 2, 3] == [2, 1, 3]

# A list can contain many types of objects
x_list = []
y_list = list()
print(x_list, y_list)
x_list.append(1)
x_list.append("something else")
x_list.append([3.14, 10])
print(x_list, x_list[2][0])

# initialize a list using for loop
for i in range(8):
    y_list.append(i**2)
print(y_list)

# initialize a list using list comprehension
x = [1, 2, 3]
y = [4, 5, 6]
z = [x[i] + y[i] for i, e in enumerate(x)]
print(z)

x_list = [i**2 for i in range(8)]
print(x_list)

off_rate = 0.2  # 20% store-wide discount
price = [10, 12, 20, 30]


def calc_discount_price(original_price):
    '''
    Apply store-weide discount to original price
    '''
    return original_price*(1 - off_rate)


new_price = [calc_discount_price(p) for p in price]
print(new_price)

# nested list comprehension
matrix = [[j * j+i for j in range(3)] for i in range(3)]
print(matrix)

# indexing and slicing
print(x_list[0], x_list[-1])
print(x_list[-2:])
print(x_list[::-1])  # reverse a list
print(x_list[10])  # out of range index; error
print(x_list[9:11])  # out of range; no error
print(x_list[-100:5])  # out-of-bound slicing

# operators +, *, in, not in
x_list = ["Apple", "Orange"] + [1, 2]
x_list = ["Apple", "Orange"] + 10  # invalid
y_list = 3*[3]
print(x_list, y_list)

if "Apple" in x_list:
    print(x_list)

if "Apple" not in y_list:
    print(y_list)

# len(), min(), max()
len(x_list)
min(x_list)  # invalid
x_list = ["Apple", "Orange", "apple"]
min(x_list)
max(x_list)

# [:] returns a new object
x_list = ["Apple", "Orange"] + [1, 2]
print(x_list, id(x_list))
y_list = x_list[:]
print(y_list == x_list, y_list is x_list)

y_list = x_list.copy()
print(y_list == x_list, y_list is x_list)

# lists are mutable
x_list = ["Apple", "Orange", "apple", "kiwi"]
x_list[0] = 2  # lists are mutable
del x_list[2]  # remove an item
x_list[:2] = ["Tomato", "Avocado"]  # modify multiple items
x_list[1:2] = [1, 2, 3, 4]  # the nubmer of items does not need to match
x_list[1] = [1, 2, 3, 4]
x_list[1:3] = []  # delete multiple elements out of the middle of a list

x_list = ["Apple", "Orange"]
x_list.append("apple")
x_list.append(["kiwi", "melon"])  # differnt from +

x_list = ["Apple", "Orange"]
x_list.extend("apple")
x_list.extend(["kiwi", "melon"])

x_list = ["Apple", "Orange", "Orange"]
x_list.insert(1, "Avocado")
# x_list.remove('apple')  #ValueError
x_list.remove('Orange')
print(x_list)
y_str = x_list.pop(1)
print(x_list, y_str)
y_str = x_list.pop(2)  # IndexError

x_list.clear()
print(x_list)

# search in a list
x_list = ["Apple", "Orange", "Orange"]
x_list.index('Orange')
x_list.index('kiwi')  # ValueError
x_list.count("Orange")
x_list.count('kiwi')

# files
import os
# in the below lines, change the directory name to one on your computer
current_dir = os.getcwd()  # check working directory
os.chdir('C:/Users/guanglan/Dropbox/BUwork/Python/CS521/')  # change it
current_dir = os.getcwd()
os.mkdir('test')  # create a single subdirectory
os.rmdir('test')  # remove a directory
os.rename('a.txt', 'b.txt')  # rename your file
os.remove('c.txt')  # remove a file

os.listdir(current_dir)
os.listdir('C:\\Users\\guanglan\\Dropbox\\BUwork\\Python\\CS521')

for filename in os.listdir(current_dir):
    if filename.endswith(('.txt', '.csv')):
        print(filename)

# filename = os.path.join(current_dir, 'd.txt')
filename = 'd.txt'
with open(filename, 'r') as d_file:
    data = d_file.read()  # read in all the content
d_file.close()

d_file = open(filename, "r")
data = d_file.read()
d_file.close()

d_file = open(filename, "r")
data = d_file.read(10)  # read the next 10 characters
print(d_file.tell())
data1 = d_file.read(10)
print(d_file.tell())
d_file.close()
print(data, data1)

# print out the top 3 lines
d_file = open(filename, "r")
i = 0
for line_str in d_file:
    if i < 3:
        print(line_str, end="")
    i += 1
d_file.close()

d_file = open(filename, "r")
i = 0
while i < 3:
    print(d_file.readline(), end="")  # read one line at a time
    i += 1
d_file.close()

d_file = open(filename, "r")
lines = d_file.readlines()  # read all lines into a list
d_file.close()
print(lines[:3])

temp_file = open('temp.txt', "w+")
x_str = "Yesterday all my troubles seemed so far away.\n" + \
        "Now it looks as though they're here to stay.\n" + \
        "Oh, I believe in yesterday.\n"
temp_file.write(x_str)  # read all lines into a list
temp_file.close()

# work with csv files
import csv
with open('senate.csv', mode='r') as senate_file:
    # csv.reader() return each row as a list of strings
    csv_reader = csv.reader(senate_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} worked in {row[3]} \
                  as a senate for {row[1]} years.')
            line_count += 1
    print(f'Processed {line_count} lines.')
senate_file.close()

with open('senate.csv', mode='r') as senate_file:
    # csv.DictReader() return each row as a dictionary
    csv_reader = csv.DictReader(senate_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["Name"]} worked in {row["State"]} as a senate \
              for {row["Years_in_office"]} year.')
        line_count += 1
    print(f'Processed {line_count} lines.')
senate_file.close()

with open('test.csv', mode='w') as test_file:
    test_writer = csv.writer(test_file, delimiter=',')
    test_writer.writerow(['Name', 'DOB', 'School'])
    test_writer.writerow(['John Smith', '11/01/1980', 'MET'])
    test_writer.writerow(['Amy Allen', '12/15/1981', 'MET'])
test_file.close()

with open('test1.csv', mode='w') as test_file:
    columns = ['Name', 'DOB', 'School']
    writer = csv.DictWriter(test_file, fieldnames=columns)

    writer.writeheader()
    writer.writerow({'Name': 'John Smith',
                     'DOB': '01/01/1989', 'school': 'MET'})
    writer.writerow({'Name': 'Erica Meyers',
                     'DOB': '12/10/1990', 'School': 'CAS'})
test_file.close()
