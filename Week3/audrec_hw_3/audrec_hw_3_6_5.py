#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 05-April-2021
Homework Problem #: 3.6.5
Description:
This program check if the input file exists, check if its content words are
less than 20 words, then write these words into four lines in another file.
"""
# Import sys modules for exiting the program
import sys

# Create constant variables with their values
TOTAL_WORDS = 20
EACH_LINE = 5

# Test the input file for existence
try:
    f = open('my_file.txt')
    print('file exists!')
    f.close()
# If the input file is not exists, print error message
except FileNotFoundError:
    print("File doesn't exist! Creating a new file now...")

# Open the file and input 20 words, create the file if it's inexisted
my_file = open('my_file.txt', "w+")
x_str = """Lorem Ipsum is simply dummy text of the printing and typesetting 
industry Lorem Ipsum has been the industrys standard dummy"""
my_file.write(x_str)
# Close the file after writing words into the file
my_file.close()

# Open the file with reading mode
file = open('my_file.txt', 'r')
# Split the read-in string by space and assign to the variable words
data = file.read()
words = data.split()

# If the total words count is not 20, exit the program
if len(words) != TOTAL_WORDS:
    print('Error: The sentence in the file does not has 20 words.')
    sys.exit()

# Open a new file to write, overwrite the content if it already exisits
new_file = open('new_file.txt', 'w+')
begin = 0
while (begin + EACH_LINE <= len(words)):
    add_str = " ".join(words[begin:begin + EACH_LINE])
    new_file.writelines(add_str + '\n')
    begin += EACH_LINE
# Close the file after write in the contents
new_file.close()


    



