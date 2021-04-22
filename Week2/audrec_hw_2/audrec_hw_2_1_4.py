#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 29-Mar-2021
Homework Problem #: 2.1.4

This program prompts for a number, converts the input to an 
integer and prints the number 0 if the user input is even and 
the number 1 if the user input is odd.
"""

# Take input and convert to integer value
input_str = input("Please enter an integer: ")
input_int = int(input_str)
# Print 0 if the input is even, print 1 if the input is odd 
print(int(input_int % 2 == 1))