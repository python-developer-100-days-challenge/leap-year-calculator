#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Leap Year Calculator
# This program takes a year as input and checks if it's a leap year or not.

# Get the year from the user
year = int(input("Which year do you want to check? "))

# Check for leap year conditions
if year % 4:
    print("Not leap year.")
elif year % 100:
    print("Leap year.")
elif year % 400:
    print("Not leap year.")
else:
    print("Leap year.")

