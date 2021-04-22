#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 29-Mar-2021
Homework Problem #: 2.1.3

This program prompts for a number, converts the input to an 
integer and make a calculation on it. Print the result with 
comma separation and with the desired format.
"""
# Function to apply the calculation
def calc_num(n):
    n = n + n ** 2 + n ** 3 + n **4
    return n
     

# Take input and convert to integer value
input_str = input("Please enter an integer: ")
input_int = int(input_str)
# Calculate by calling calc_num function and assign to the variable result
result = calc_num(input_int)

# Add comma separator if the result is greater than 1000
if result > 1000:
    result = "{:,}".format(result)

# Print the output in the desired format
print("{0} + {0} * {0} + {0} * {0} * {0} + {0} * {0} * {0} * {0} = {1}".format(input_str, result))

