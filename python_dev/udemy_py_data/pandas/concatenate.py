#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:28:48 2016

@author: danielbillmann
"""

#concatenate.py

import os
import glob
import pandas

#will generate a dataFrame
def concatenate(indir="/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/pandas/CSV-Files",outfile="concatenate.csv"):
    os.chdir(indir)
    fileList=glob.glob("*.csv")
    colNames=["Year", "Month", "Day", "Hour", "Temp", "DewTemp", "Pressure", "WindDir", "WindSpeed","Sky","Precip1", "Precip6","ID"]
    dfList=[]
    for filename in fileList:
        print(filename)
        df=pandas.read_csv(filename, header=None)
        dfList.append(df)
    cdf = pandas.concat(dfList,axis=0)
    cdf.columns=colNames
    cdf.to_csv(outfile,index=None)
    