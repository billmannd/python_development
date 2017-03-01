#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 13:55:19 2016

@author: danielbillmann
"""
intl_students = input("What percentage of international students are there? ")
intl_student_rating = 0
done = True

try:
    while done == True: 
        intl_students = int(intl_students)
    
        if intl_students > 100:
            print("Please enter an integer from 0 to 100: ")
            
        elif intl_students > 80:
           intl_student_rating = 1
           done = False
        elif intl_students > 60:
            intl_student_rating = 3
            done = False
        elif intl_students > 40: 
            intl_student_rating = 5
            done = False   
        elif intl_students > 20:
            intl_student_rating = 7
            done = False
        else: 
            intl_student_rating = 10
            done = False  
except:
    print('please enter a number: ')
print(intl_students)
print(intl_student_rating)

'''
    
'''