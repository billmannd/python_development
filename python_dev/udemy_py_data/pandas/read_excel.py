#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 23:04:39 2016

@author: danielbillmann
"""

import os
import pandas

os.getcwd()
currDir= "/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/"
df = pandas.read_excel("Boulder2016.xlsx", sheetname=0)
space = currDir+"Space-Separated.txt"
df1 = pandas.read_csv(space.split(" "))

#run df.head() in the console to 