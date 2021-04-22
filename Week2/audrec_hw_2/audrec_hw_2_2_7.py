#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 29-Mar-2021
Homework Problem #: 2.2.7

This program rewrites a program that prints all factor of 10 within range 1 to 10 
from for-loop to while-loop.
"""
# Create a constant X with value 10
X = 10

# Initialize i from value 1
i = 1
# Print out all the factors of the constant X within range 1 to X
while i <= X:
    if X % i == 0:
        print(i)
    i += 1

