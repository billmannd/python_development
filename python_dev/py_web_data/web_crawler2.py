#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Additional web crawler with search function

Created on Thu Dec 15 12:55:49 2016

@author: danielbillmann
"""

import urllib.request
import re

# Web Crawler Function
def crawl():
    webpage = input("Please enter a URL: ")
    with urllib.request.urlopen(webpage) as response:
        html = response.read()
    return html


    
    
# Search function that takes an HTML file as an input
def searchPage(html):
    keyword = input("Please enter the keyword you wish to search: ")
    blah = re.compile(html)
    oink = re.search(blah, '\bkeyword\b')
    print(oink)
 
crawl()
print(html)
#searchPage(html)
#html = crawl()
#offer option to search within the webpage
#webpage_search = input("Would you like to search the webpage? ").lower()
#if webpage_search == "yes" or webpage_search == "y": 
 #   print(html)
    
    
