#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 12-April-2021
Homework Problem #: 4.9.3
Description:
This program takes in one list of first names and one list of last names,
return a dictionary from combining two lists.
"""
# Import sys module for exiting the program
import sys

# Set constant first name list and last name list
FIRST_NAME_LIST = ['Jane', 'John', 'Jack']
LAST_NAME_LIST = ['Doe', 'Deer', 'Black']

def name_dict_factory(first_name, last_name):
    '''Create a dictionary by zipping last name list and first name list'''
    name_dict = dict(zip(last_name, first_name))
    # If two lists' length is unequal, quit the program
    if len(last_name) != len(first_name):
        sys.exit('The length of two lists are not equal, program exit now.')
    return name_dict

# Print out the original first name list and last nmae list
print(f'First Names: {FIRST_NAME_LIST}')
print(f'Last Names: {LAST_NAME_LIST}')
# Get the dictionary of two lists by calling dict factory function
result = name_dict_factory(FIRST_NAME_LIST, LAST_NAME_LIST)
print(f'Name Dictionary: {result}')
        
