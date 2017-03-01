# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os, pandas, numpy, scipy, plotly, plotlib,seaborn
os.getcwd()

file = "/Users/danielbillmann/Downloads/RTF+280+Brand+Positioning+Survey_October+31%2C+2016_07.13.csv"
with open(file, "r") as file:
    df = pandas.read_csv(file)
