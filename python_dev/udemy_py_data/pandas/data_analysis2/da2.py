# -*- coding: utf-8 -*-
filename = "/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/pandas/data_analysis2/IncomeByState1984.csv"
worldIncome = "/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/pandas/data_analysis2/WorldIncome1984.csv"
import pandas
df=pandas.read_csv(filename, skiprows=3)
df=df.dropna(axis=1, how='all')
df['1984'].astype(float)
#df["1984 Euros"]=df['1984'].astype(.replace(',',''))
#df["1984 Pounds"]=df['1984'].*.64
df.to_csv(worldIncome,index=None)