#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 16:36:45 2016

@author: danielbillmann
"""

import random

rand = random.randint(0,100)
print("Hello, I am ", rand, "years old.")
time = input("What time is it?")
time = int(time)

if time >=10 or time <= 2: 
    if rand < 21: 
        print ("You are not allowed in the bar")
    elif rand < 35: 
        print ("We are going to need to check your ID \n\n\nWelcome to Dan's Tiki Bar!")
    else:
        print ("Welcome to Dan's Tiki Bar!")
else: 
    if rand < 16:
        print("You must be accompanied by an adult of legal drinking age")
    elif rand < 21: 
        print("You are not allowed to drink, but can stay until 10PM")
        dd = input("Are you a designated driver? Y or N?")
        dd.lower()
        if dd == "y":
            print("Great! Thank you so much. We will need to mark your hands so you can get free fountain drinks.")
    elif rand < 35:
        print("We are going to need to see some ID\n\n\n Welcome to Dan's Tiki Bar!")
    else: 
        print("Welcome to Dan's Tiki Bar!")