#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:09:32 2016

@author: danielbillmann
"""

merchandise = "denver"

airport = "denver"


def passReaction(): 
    reaction = "oh shit"
    print(reaction)
    return reaction

def dmitryReaction(): 
    reaction = "Oh shit!"
    print(reaction)
    return reaction

if airport == merchandise:
    # I concatenated (aka smooshed) the string "welcome to" with the value of 
    # "airport". That way no matter what airport you want it will print that out!
    print("Welcome to ", airport)
else: 
    passReaction()
    dmitryReaction()