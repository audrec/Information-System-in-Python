#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 29-Mar-2021
Homework Problem #: 2.2.6

This program calculates and prints all the leap years from 1899 to 2021 using for-loop 
and while-loop.
"""
# Create a list to store the leap year
list_1 = []

# Calculates and prints leap years using for-loop filtered with if condition  
for year in range(1899, 2022):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400 == 0):
                list_1.append(str(year))
        else:
            list_1.append(str(year))

# Print the result with comma separated each element in the list        
result = ','.join(list_1)      
print(result)


# Create a list to store the leap year
list_2 = []
# Initialize the year variable with value 1899
year = 1899
                
# Calculates and prints leap years using while-loop filtered with if condition 
while year >= 1899:
    # Break the while-loop when year reaches 2022
    if (year == 2022):
        break
    if (year % 4) == 0:
        if (year % 100 == 0):
            if (year % 400 == 0):
                list_2.append(str(year))
        else:
            list_2.append(str(year))
    # Add 1 to the year variable for each iteration
    year += 1

# Print the result with comma separated each element in the list 
result_2 = ','.join(list_2)         
print(result_2)
                