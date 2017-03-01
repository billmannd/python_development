#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 10:32:04 2016

@author: danielbillmann
"""

import pandas, os
os.getcwd()
da = pandas.read_excel("Income-By-State-1984 (1).xls", sheetname="h08", skiprows=[0,1,2])
da.to_csv("StateIncome1984.csv", index=0)