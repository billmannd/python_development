#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:23:09 2016

@author: danielbillmann
"""
#calculating and adding columns to .csv files
import os, pandas, glob

def addField(indir = "/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/pandas/All-Data-Files"):
    os.chdir(indir)
    fileList = glob.glob("*")
    for filename in fileList:
        df = pandas.read_csv(filename,sep='\s+',header=None)
        df["Station"] = [filename.rsplit("-",1)[0]]*df.shape[0]
        df.to_csv(filename+".csv",index=None, header=None)
addField()