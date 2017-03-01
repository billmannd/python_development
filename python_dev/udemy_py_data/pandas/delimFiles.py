#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 11:45:22 2016

@author: danielbillmann
"""

import os
import pandas

os.getcwd()
currDir= "/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/"

comma = currDir + "Comma-Separated.txt"
space = currDir + "Space-Separated.txt"

df_comma = pandas.read_csv(comma,index_col=3)
# .head() must be run in python interface
df_comma.head()

df_space = pandas.read_csv(space, ' ')
# .head() must be run in python interface
df_space.head()

