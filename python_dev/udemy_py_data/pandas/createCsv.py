#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:36:30 2016

@author: danielbillmann
"""
import os
#os.chdir("/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/pandas/data_analysis2")
fileName = input()
csv = os.path.splitext(fileName)[0]

csv = csv + ".csv"
print(csv)
open(csv, 'r').close()
