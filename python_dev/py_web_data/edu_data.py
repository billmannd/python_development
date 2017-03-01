#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:46:23 2017

@author: danielbillmann
"""

from urllib.request import urlopen
import pandas as pd
url = 'https://inventory.data.gov/api/action/datastore_search?resource_id=38625c3d-5388-4c16-a30f-d105432553a4&limit=5&q=title:jones'
data = pd.read_html(url)