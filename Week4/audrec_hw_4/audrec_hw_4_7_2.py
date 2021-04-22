#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 12-April-2021
Homework Problem #: 4.7.2
Description:
This program calculates the sum of list's each element's nearest neighbors 
and itself from the original list.
"""
# Set a constant list of integers
CONS_LIST = [10, 20, 30, 40, 50]

def sum_neighbors(list):
    '''Takes in a list, return the sum of neighboring elements with new list'''
    new_list = []
    # First element only needs to add element in index 1
    new_list.append(list[0] + list[1])
    x = 1
    # Loop until the last two element in the list
    while x < len(list) - 1:
        # Add neighboring elements with each element in the list
        new_list.append(list[x - 1] + list[x] + list[x + 1])
        x += 1
    # The last element only needs to add its previous element
    new_list.append(list[x - 1] + list[x])
    return new_list

# Print out the original list
print(f'Input List: {CONS_LIST}')
# Get the result of addition of each neighboring elements and itself
result = sum_neighbors(CONS_LIST)
print(f'Result List: {result}')
