#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:09:32 2016

@author: danielbillmann
"""


unbroken = True

#this function breaks the vase by changing "unbroken" from = 'True' to 'False' 
def breakVase():
    unbroken = False
    print("You're going to get it!")
    return unbroken

#this function fixes the vase by changing "unbroken" to 'True'
def fixVase():
    unbroken = True
    print("You gotta fix that now!")
    return unbroken

    
    
# if tellingTheTruth != myWords
# call me a liar

# if the vase is broken
# fix the vase

# if the vase is not unbroken
# fix the vase
    
if unbroken!= 0:
    fixVase()

elif unbroken!=False:
        breakVase()   
        
elif unbroken=="orange":
    print("Yep it's orange")
else: 
    print("what the fuck that doesn't make sense")