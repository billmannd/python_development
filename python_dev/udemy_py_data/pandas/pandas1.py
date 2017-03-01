#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 10:56:25 2016

@author: danielbillmann
"""

import os, pandas
os.chdir("/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/")
df = pandas.read_csv("SmallFile.csv", index_col=0)
df
bo = df.loc["Day 2":"Day 4", "Month":"Hour"]