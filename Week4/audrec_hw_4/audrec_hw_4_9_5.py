#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yen-Chi Chen
Class: CS 521 - Spring 2
Date: 12-April-2021
Homework Problem #: 4.9.5
Description:
This program takes in a string and return a dictionary with each character as
its key and character's count as its value. It also finds the most frequent 
character and prints the histogram by the frequency the char appears.
"""
# Create a constant string for the input
TARGET_STRING = "WWWAS IT A RAT I SAW"

def letter_count(s):
    '''takes a string as its argument and returns a dictionary of the letters 
    as keys and frequency counts as values'''
    letter_dict = {}
    for c in s:
        if c != ' ':
            letter_dict[c] = letter_dict.get(c, 0) + 1
    return letter_dict

def most_common_letter(s):
    '''takes a string and returns a string of the most common letter(s)''' 
    target_dict = letter_count(s)
    freq = 0
    k_list = []
    # Keep updating the count of each key when encounting a bigger value
    for k, v in target_dict.items():
        if v > freq:
            freq = v
    for k, v in target_dict.items():
        if v == freq:
            k_list.append(k)
    return k_list, freq

def string_count_histogram(s):
    '''takes a string and returns a list of the unique letters, with each 
    letter being the repeated number of times it appears in the string.''' 
    target_dict = letter_count(s)
    unique_list = []
    for k, v in target_dict.items():
        unique_list.append(k * v)
    return unique_list

# This block's code will run if this module is the entry point to the program
if __name__ == '__main__':
    # Print the analyzed string first
    print(f'The string being analyzed is: {TARGET_STRING}')
    # Get the character count dict by calling a function
    char_dict = letter_count(TARGET_STRING)
    print(f'1. Dictionary of letter counts: {char_dict}')
    # Get the most frequent character by calling a function
    most_freq_letter, freq = most_common_letter(TARGET_STRING)
    # Print the result in a desired format
    print(f'2. Most frequent letter {most_freq_letter} appears {freq} times')
    # Get the histogram list by calling a function
    histogram = string_count_histogram(TARGET_STRING)
    # Set each list element in its own line
    one_line = '\n'.join(map(str, histogram))
    print('3. Histogram: ')
    print(one_line)
    