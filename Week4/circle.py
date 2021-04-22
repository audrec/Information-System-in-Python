# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:27:45 2021

@author: guanglan
"""
# prompt user to input a numeric value as the radisu of a circle
# Calculate the circle's circumference and area and print them out

import calc_circle_circumference_area as calc_circle

while True:
    in_str = input("Enter a numeric value as the radius of a circle:")

    try:
        circum, area = calc_circle.circum_area(float(in_str))
        print(f"The circumference is {circum} and area is {area}")
    except ValueError:
        print("Wrong input. Cannot cast: ", in_str)
        continue
    else:
        # circumference and area are calculated. Ready to exit the loop.
        break
