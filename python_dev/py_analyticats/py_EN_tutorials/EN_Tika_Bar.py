#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:29:04 2016

@author: danielbillmann
"""

import random

me = "Emmalese"

age = random.randint(0,100)
time = random.randint(0, 24)

print("I am ", age, "years old.")
print(time)

if 16 <= time <= 24 or 0 <= time <= 2:
    print("The bar is open")
    if 22<= time <=24 or 0 <= time <= 2:
        print("After 10 PM")
        if age <= 35:
            print("Check ID")
            if age > 21: 
                print("Welcome to Dan's Tiki Bar!")
            else: 
                print("You must leave now.")
        else: 
            print("You're in!")
    else: 
        print("Before 10PM")
        if age > 35: 
            print("You're in!")
        else:
            print("Check ID")
            if age >= 21: 
                print("Welcome")
            else: 
                if age < 18:
                    if age < 16:
                        print("Parent or guardian required")
                    else: 
                        print("You're allowed in")
                else: 
                    print("You are allowed in.")
                
else: 
    print("The bar is closed, please come back later.")