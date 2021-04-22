#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 05-April-2021
Homework Problem #: 3.2.1
Description:
This program counts the number of odd numbers, even numbers, squares of an 
integer and cubes of an integer from 2 to 130 (inclusive).
"""

# Set the range by using constants
START = 2
END = 130

# Initialize variables for counting odd, even, square, cube numbers
odd_count = 0
even_count = 0
first_odd = 0
last_odd = 0
first_even = 1
last_even = 1
square_count = 0
cube_count = 0

# Initialize an empty list for storing square and cube numbers
square_list = []
cube_list = []

# Cheking numbers within the range
for num in range(START, END + 1):
    # Check square number within the range and add to the list
    if num * num <= END:
        square_count += 1
        square_list.append(num * num)
    # Check cube number within the range and add to the list
    if num * num * num <= END:
        cube_count += 1
        cube_list.append(num * num * num)
    # Check for odd numbers, update counts, first and last odd number
    if num % 2 == 1:
        if first_odd == 0:
            first_odd = num
        if num > last_odd:
            last_odd = num
        odd_count += 1
    # Check for even numbers, update counts, first and last even number
    elif num % 2 == 0:
        if first_even == 1:
            first_even = num
        if num > last_even:
            last_even = num
        even_count += 1
        
print(f"""
      Checking numbers from {START} to {END} \n
      Odd ({odd_count}) : {first_odd}...{last_odd} \n
      Even ({even_count}): {first_even}...{last_even} \n
      Square ({square_count}): {square_list} \n
      Cube ({cube_count}): {cube_list}
      """)

        
