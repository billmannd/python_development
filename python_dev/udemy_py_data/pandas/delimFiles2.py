#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas

cs = pandas.read_csv("Comma-Separated.txt", sep=',')
cs.to_csv("Comma-Separated.csv")
cs = pandas.read_csv("Comma-Separated.csv", " ")
cs.to_txt