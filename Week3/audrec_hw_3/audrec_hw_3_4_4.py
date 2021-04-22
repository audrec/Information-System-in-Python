#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 05-April-2021
Homework Problem #: 3.4.4
Description:
This program takes in a three-digit whole number and check if the digits are 
in ascending order and without containing duplicated digits.
"""

def check_len(s):
    '''Takes in a string, return if this string's length is 3'''
    return len(s) == 3

def check_integer(s):
    '''Takes in a string, return if this string is an integer'''
    return s.isnumeric()

def check_ascending(s):
    '''Takes in an int, check if no duplicated digits and in ascending order'''
    i = 0
    while i < len(s) - 1:
        # Check duplicated digit
        if ord(s[i + 1]) == ord(s[i]):
            print('Your number contains duplication.')
            return False
            break
        # Check descending digit
        elif ord(s[i+1]) < ord(s[i]):
            print('Error: The digits are not in ascending order.')
            return False
            break
        else:
            i += 1
    return True
     
while True:
    # Prompts the user to enter a three-digit whole number
    input_str = input('Please enter a 3-digit integer: ')
    
    # Back to input prompts if it's not a valid integer
    if not check_integer(input_str):
        print('Error: This is not an integer. Please re-enter.')
        continue
    # Back to input prompts if it's not a 3-digit integer
    if not check_len(input_str):
        print('Error: You did not enter a 3-digit number.')
        continue
    # Back to input prompts if it's not a valid integer
    if not check_ascending(input_str):
        continue
    # Found a valid input, break the prompt
    else:
        print('Number Accepted!')
        break
    
    
            
    
    


