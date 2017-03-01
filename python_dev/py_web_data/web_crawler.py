#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:39:22 2016
Completed on: Wed Dec 14 16:40:80 2016
@author: danielbillmann

web crawler 1.0
r    
"""
import urllib.request
import re

def ex():
    raw_html = input('type a URL here --> ')
    crawler_out = open('crawler_out.txt', 'w')
    with urllib.request.urlopen(raw_html) as response:
        html = str(response.read())

        for line in html:
            cleanT = re.compile('<.*?>')
            lineBreak = re.compile('\n')
            cleanText = re.sub(cleanT, '', html)
            cleanText = re.sub(lineBreak,'\n',html)
            print(cleanText)
            crawler_out.write(cleanText)
        crawler_out.close()            

ex()

    
