#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

boulder = pd.read_excel('Boulder2016.xlsx')
#pre2000temp = boulder[(boulder['Year']<2000) & (boulder['Month']=='JAN')]['Temperature'].mean()

temps = np.array(boulder['Temperature'])
time = np.arange(0,len(temps))
#Full Temperatures in Boulder Colorado
'''
plt.plot(time, temps, 'r')
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.title('Boulder, CO temperatures 1991-Present')
plt.show()
'''
#Annual Temperatures in Boulder Colorado
'''
annual_temps = np.array(boulder.groupby('Year').mean())
years = np.array(boulder['Year'].unique())

plt.plot(years, annual_temps,'b')
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Annual Average Temperatures in Boulder CO')
plt.show()
'''
#Avg temperature by month
annual_temps = np.array(boulder.groupby('Month')['Temperature'].mean())
months = np.arange(0,len(annual_temps))

plt.plot(months, annual_temps,'b')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.title('Temperatures in Boulder CO by Month')
plt.show()
