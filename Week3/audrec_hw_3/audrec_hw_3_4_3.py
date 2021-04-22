#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 05-April-2021
Homework Problem #: 3.4.3
Description:
This program counts the number of uppercase letters, lowercase letters, digits
, and punctuations of the input string, then print out a list about it.
"""
# Import string module for string operation
import string

def check_upper(s):
    '''Takes in a string, and return if it is the uppercase letter'''
    return s.isupper()
    

def check_lower(s):
    '''Takes in a string, and return if it is the lowercase letter'''
    return s.islower()

def check_digits(s):
    ''' Takes in a string, and return if it is the digit'''
    return s.isdigit()

def check_punc(s):
    '''Takes in a string, and return if it is the punctuation'''
    return s in string.punctuation

# Initialize variables for the count of each categories        
upper_count = 0
lower_count = 0
digit_count = 0
punc_count = 0        

# Prompts the user for a sentence
input_str = input('Enter a sentence with uppercase letters, lowercase letters'
                  + ', digits, and punctuation: ')

# Loop through the input string, update count if it's a valid check
for ele in input_str:
    if check_upper(ele):
        upper_count += 1
    elif check_lower(ele):
        lower_count += 1
    elif check_digits(ele):
        digit_count += 1
    elif check_punc(ele):
        punc_count += 1

# Initialize column names of the list
col1 = "# Upper"
col2 = "# Lower"
col3 = "# Digits"
col4 = "# Punct. "
seps = "--------"

# Output and print the summarized list in the desired format
print(f"""
      {col1 : ^10} {col2 : ^10} {col3 : ^10} {col4: ^10} 
      {seps : ^10} {seps : ^10} {seps : ^10} {seps: ^10} 
      {upper_count: ^10} {lower_count: ^10} {digit_count: ^10} {punc_count: ^10}
      """)




