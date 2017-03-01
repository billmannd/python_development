#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 00:25:10 2016

@author: danielbillmann
"""
import numpy as np
import pandas as pd
import lxml
import html5lib
from bs4 import BeautifulSoup
from collections import OrderedDict

#url='http://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-rpi'
url='http://www.espn.com/mens-college-basketball/rpi/_/sort/RPI'
rpi = pd.read_html(url)
rank = rpi[0][0]
team = rpi[0][1]
rpi_score = rpi[0][2]
rankings = []

for r in rank: 
    try:
        if r.isdigit():
            rankings.append(int(r))
    except AttributeError:
        if type(r) is float:
            rankings.append(rankings[len(rankings)-1])
        else:
            print(type(r))
        continue

rankings = np.array(rankings)
team = np.array(team)
team_ranking = []
tr= []
for r in range(0,len(rankings)):
    team_ranking.append({"Team":team[r],"Ranking": rankings[r],"RPI":rpi_score[r]})
for r in range(0,len(team_ranking)):    
    if r!=1 or (r-1)%11!=0 or r!=0:
        tr.append(team_ranking[r])
print(tr)