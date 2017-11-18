#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 22:44:07 2017

@author: Dan Billmann
"""

from setuptools import setup

setup(
    name='flaskr',
    version='1.0',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
)
