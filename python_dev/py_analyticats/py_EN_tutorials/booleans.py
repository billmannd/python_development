# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

unbroken = True
#boom = True
#print(boom)
def breakVase():
    unbroken = False
    print("You're going to get it!")
    return unbroken

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

def checkMech(merchandise, airport): 
    
    def passReaction(): 
        reaction = "oh shit"
        print(reaction)
        return reaction
    
    def dmitryReaction(): 
        reaction = "damn it!"
        print(reaction)
        return reaction
    
    if airport == merchandise:
        print("Welcome to denver")
    else: 
        passReaction()
        dmitryReaction()

#checkMech("denver", "portugal")
