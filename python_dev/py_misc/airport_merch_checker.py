#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:46:20 2016

@author: danielbillmann
"""
# declares a function that asks for the [location of the] merchandise and airport

def checkMerch(merchandise, airport): 
    
    def passReaction(): 
        reaction = "oh shit"
        print(reaction)
        return reaction
    
    def dmitryReaction(): 
        reaction = "damn it!"
        print(reaction)
        return reaction
    
    if airport == merchandise:
        print("Welcome to " + str(airport))
    else: 
        passReaction()
        dmitryReaction()

# calls the function "checkMerch"
# if you remember from the top we need to tell checkMerch which merchandise
# and airport to check 
checkMerch("denver", "portugal")

# prints oh shit and damn it! because we asked checkMerch to compare denver to portugal
'''
the original function is like a template for what we want to do
in  checkMerch(merchandise, airport) merchandise and airport are each placeholders
for values we ACTUALLY want to check. 

when we call the method checkMerch("denver", "portugal") we swap in "denver" for
merchandise and "portugal" for airport.

by writing the function checkMerch(merchandise, airport) with placeholders, we are
not restricted to just "denver" or "portugal" or "Cincinnati", etc. We can check 
any of them. 

'''

# we can add in user input by using the "input()" method

merch = input("What city's merchandise would you like to buy? ")
aeropuerto = input("What city are you flying into? ")

checkMerch(merch, aeropuerto)

#this allows us to choose which city to check against!