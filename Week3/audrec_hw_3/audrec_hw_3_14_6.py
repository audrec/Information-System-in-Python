#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 05-April-2021
Homework Problem #: 3.14.6
Description:
This program check if the input file exists, write in the input,
read the file line by line, write each line into a list, and put and print
these lists of lists as the result.
"""
# Test the input file for existence
try:
    f = open('student_records.txt')
    print('file exists!')
    f.close()
# If the input file is not exists, print error message
except FileNotFoundError:
    print("File doesn't exist! Creating a new file now...")

# Open the file and input 20 words, create the file if it's inexisted
my_file = open('student_records.txt', "w+")
my_file.writelines("Tyrion Lannister, 1, 3.7\n")
my_file.writelines("Daenerys Targaryen, 52, 2.8\n")
my_file.writelines("Jon Snow, 13, 3.9\n")
my_file.writelines("Sansa Stark, 24, 3.4\n")
# Close the file after writing words into the file
my_file.close()

# Initialize an empty list for the result list
result_list = []
# Open the file and read it line by line
with open('student_records.txt') as file:
    for line in file:
        # Initialize an empty list for each single list
        single_list = []
        # Strip each line by \n
        line = line.strip()
        # Append this line to the single_list
        single_list.append(line)
        # Append each single_list to the result_list
        result_list.append(single_list)


# Close the file when finished the operation on it
file.close()

# Print the result in the format of list of list
print(result_list)

