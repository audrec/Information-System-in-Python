#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 12-April-2021
Homework Problem #: 4.9.4
Description:
This program creates key list and value list from the input dictionary, and
return the result of dictionary sorted by keys and values.
"""
# Create a constant dictionary 
MY_DICT = {'a':15, 'c':18, 'b':20}

# Initialize keys list and values list to store keys and values
keys_list = []
values_list = []

def generate_lists(list):
    '''iterate the dictionary and add each key to key list, add
    each value to value list'''
    for k, v in list.items():
        keys_list.append(k)
        values_list.append(int(v))
    return keys_list, values_list

def first_index(x):
    '''get the data at index 1'''
    return x[1]

keys_list, values_list = generate_lists(MY_DICT)
# Combine key list and value list to a key value dictionary
key_value_dict = dict(zip(keys_list, values_list))
        
print(f'Keys: {keys_list}')
print(f'Values: {values_list}')
print(f'Key value pairs: {key_value_dict}')
# Sort the dictionary by key
sort_by_key = dict(sorted(key_value_dict.items()))
print(f'Key value pairs ordered by key: {sort_by_key}')
# Sort the dictionary by value
sort_by_value = dict(sorted(MY_DICT.items(), key = first_index))
print(f'Key value pairs ordered by value: {sort_by_value}')


    
