#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:40:56 2016

@author: danielbillmann
"""
import os

def convertCSV():
    f = input("What's the path of the file? ")
    if os.path.splitext(f)[1] == ".csv":
        print(f)
    else:
        f = os.path.splitext(f)[0]+ ".csv"
        os.open(f, "a")
    return f
convertCSV()