#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 10:08:58 2016

@author: danielbillmann
"""

import pandas, os

os.chdir("/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data")
fw = pandas.read_fwf("Fixed-Width.txt")
