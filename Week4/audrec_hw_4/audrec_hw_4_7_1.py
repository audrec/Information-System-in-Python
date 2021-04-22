#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 12-April-2021
Homework Problem #: 4.7.1
Description:
This program calculates the sum of all even numbers and odd numbers in the 
range using list comprehension, and print out the result.
"""
# Set start and end point for range as constant variables
START = 1
END = 10

def even_sum(start, end):
    '''Takes in two range numbers, return sum of all even numbers in range'''
    return sum(n for n in range(start, end + 1) if n % 2 == 0)

def odd_sum(start, end):
    '''Takes in two range numbers, return sum of all odd numbers in range'''
    return sum(n for n in range(start, end + 1) if n % 2 == 1)

# Initialize an empty list for indiciating all numbers in range
range_list = []
# Adding all numbers in range to the list
for i in range(START, END + 1):
    range_list.append(i)
# Convert range list to string with comma separated each number
range_str = ', '.join(str(e) for e in range_list)

# Print all numbers in the range
print(f'Evaluating the numbers in: {range_str}')
# Calculate sum of all even numbers in range by calling function even_sum
even_result = even_sum(START, END)
print(f'Even: {even_result}')
# Calculate sum of all odd numbers in range by calling function odd_sum
odd_result = odd_sum(START, END)
print(f'Odd: {odd_result}')


