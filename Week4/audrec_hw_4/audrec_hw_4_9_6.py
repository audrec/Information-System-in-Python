#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 12-April-2021
Homework Problem #: 4.9.6
Description:
This program takes a numeric input from the user and return the alphabetic 
format of that numeric input .
"""

def int_to_eng(num):
    '''takes a number and convert it to the alphabetic format'''
    d = {'0' : 'Zero', '1' : 'One', '2' : 'Two', '3' : 'Three', '4' : 'Four', 
         '5' : 'Five', '6': 'Six', '7' : 'Seven', '8' : 'Eight', '9' : 'Nine', 
         '.' : 'Point', '-' : 'Negative'}
    convert_list = []
    for i in num:
        convert_list.append(d.get(i))
    # Convert the result list to a string
    answer = ' '.join(convert_list)
    return answer

# Keep prompting user to input a number until a valid number input
while True:
    num_input = input("Enter a numeric number: ")
    
    # If commas appears, print the error message and reprompt for input
    if ',' in num_input:
        print("Please try again without entering commas.")
        continue
    # If the input is all digit or a negative number, it is a valid input
    if num_input.isnumeric() | num_input.strip('-').isnumeric():
        break
    # If the input is a floating number, it is a valid input 
    if '.' in num_input:
        # Split input by the decimal and forms a list
        split_num = num_input.split('.')
        # If the input only contains 1 decimal and both elements in the list 
        # are numeric, it's a valid floating number input
        if len(split_num) == 2 and split_num[0].strip('-').isnumeric() and \
            split_num[1].isnumeric():
                break
    else: 
        # Print the error message for invalid input and reprompt for the input.
        print(f'"{num_input}" is not a valid number. Please try again')
        continue

# Get the result by calling int_to_eng() function and print it
result = int_to_eng(num_input)
print(f'As Text: {result}')

        

