#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 05-April-2021
Homework Problem #: 3.4.2
Description:
This program check if the constant string is of an odd length, print the 
middle character, 1st half of the string, and 2nd half of the string.
"""
# Import sys module for exiting the program
import sys

def is_odd_len(s):
    '''Takes in a string, check if it is of an odd length''' 
    return len(s) % 2 == 1
        
        
def get_middle(s):
    '''Takes in a string, return the middle character of it'''
    return (s[len(s) // 2])

def get_first_half(s):
    ''' Takes in a string, return the first half of the string'''
    return s[:len(s) // 2]

def get_last_half(s):
    '''Takes in a string, return the last half of the string'''
    return s[len(s) // 2 + 1 :]
    

# Set a constant with an odd length string
ODD_STRING = "A man a plan a canal Panama"

# If the string is of an odd length, print its length and its content
if is_odd_len(ODD_STRING):
    print(f'My {len(ODD_STRING)}-character string is: "{ODD_STRING}"')
# Otherwise, ends the program with the error message
else:
    sys.exit("The string is not of an odd length, program ends now.")

# Get the middle character and print it out
middle_char = get_middle(ODD_STRING)
print(f'The middle character is: "{middle_char}"')

# Get the 1st half of the string and print it out
first_half = get_first_half(ODD_STRING)
print(f'The 1st half of string is: "{first_half}"')

# Get the 2nd half of the string and print it out
last_half = get_last_half(ODD_STRING)
print(f'The 2nd half of string is: "{last_half}"')



