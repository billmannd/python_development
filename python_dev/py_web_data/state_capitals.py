#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 12:59:25 2017
state capitals
@author: danielbillmann
"""
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd

us_states = 'https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States'
state_data = pd.read_html(us_states)
states = state_data[0]

url = urlopen(us_states)
soup = bs(url, 'html.parser')