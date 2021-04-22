#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 29-Mar-2021
Homework Problem #: 2.1.5

This program prompts for weight and height from the user, calculate the BMI, 
then prints it with original weight and height input.
"""
# Use this function to calculate BMI
def calc_BMI(weight, height):
    return weight / height ** 2

# Take input from user for weight and height in one line and convert to float value
weight, height = input('Enter Weight in kilograms and Height in meters (separated by a space): ').split()
weight = float(weight)
height = float(height)

# Perform BMI calculation by calling calc_BMI function then round to 2 decimals
result = float(round(calc_BMI(weight, height), 2))

# Print the BMI with original weight and height input
print('Body Mass Index (BMI) for weight', weight, 'and Height', height, ':', result)
