#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 29-Mar-2021
Homework Problem #: 2.1.1

This program prompts for a number, do calculation on the input, 
then print if the result matches the expected calculated value.
"""

def calc_num(num):
    num = ((num + 2) * 3 - 6) / 3
    return num

# Take input and convert to integer.
input_str = input('Enter a numeric number: ')
input_int = int(input_str)

# Apply calc_num function to perform the calculation, and assign to the variable result
result = calc_num(input_int)

# Print messages for calculated value checks.
if (result == ((input_int + 2) * 3 - 6) / 3):
    print('The calculated value for the input ', input_str, ' is: ', result, ', which is matched to the expected result.')
else:
    print('The calculated value for the input is not matched with the expected value.')

