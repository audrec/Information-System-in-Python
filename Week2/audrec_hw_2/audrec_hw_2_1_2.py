#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 29-Mar-2021
Homework Problem #: 2.1.2

This program prompts for a number, print the input string, converts the input to an 
integer and to a float value then print them out. 
"""

# Take input from the user
input_str = input('Enter a numeric number: ')

# Cast the input to string, integer, and float value and print them out
print(input_str)
print(int(input_str))
print(float(input_str))

"""
Only integer data type can be the valid input, because integer value can be casted to both string and float value.
However, a float value will lose precision if cast to an integer value and thus will cause error. 
Input other than an integer data type will not work for this program.
"""


