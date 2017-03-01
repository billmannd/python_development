#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 17:48:25 2017

@author: danielbillmann
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import os
os.chdir('/Users/danielbillmann/Spring_2017/Intro_to_Data_Science/py_Data_Science_Machine_Learning/Machine Learning Sections/Logistic-Regression')

train = pd.read_csv('titanic_train.csv')
#train.head()
''' Exploratory Analysis
At this point we'll be doing some exploratory analysis of the dataset. However, we also may have some missing data.
To find out where we have the most missing data, we can use seaborn to make a graphic of it.
'''
train.isnull()
#sns.heatmap(train.isnull(),yticklabels=False, cbar=False, cmap='inferno')

'''
Since about 20% of the Age data is missing, we can squeeze out a result 
by fililng in those columns using other data points already available. However,
 we're missing too much Cabin data to do anything with it besides a) dropping 
the columns or b) reframing the problem to be 'columnknown - 1,0'
'''

sns.set_style('whitegrid')

#sns.countplot(x='Survived', data = train)
#add hue of sex
#sns.countplot(x='Survived', hue='Sex', data=train, palette="coolwarm")
#change hue from 'Sex' to class level
#sns.countplot(x='Survived', hue='Pclass', data=train, palette='coolwarm')

#sns.distplot(train['Age'].dropna(), kde=False, bins=30)

#pandas way of doing this
train['Age'].plot.hist()


train.info()
#sns.countplot(x='SibSp', data=train)
train['Fare'].plot.hist(bins=40, figsize=(10,4))

#Interactive plot
'''#import cufflinks as cf
#cf.go_offline()
#train['Fare'].iplot(kind='hist', bins=50)
'''
#sns.boxplot(x='Pclass', y='Age', data=train)

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age

train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)
#sns.heatmap(train.isnull(),yticklabels=False, cbar=False, cmap='viridis')
train.drop('Cabin', axis=1, inplace=True)
train.dropna(inplace=True)
#sns.heatmap(train.isnull(),yticklabels=False, cbar=False, cmap='viridis')

## train.head()

'''
# Categorization Values
Now we're done cleaning the data, we'll need to break it into categories
'''
sex = pd.get_dummies(train['Sex'], drop_first=True)
embark = pd.get_dummies(train['Embarked'], drop_first=True)
train = pd.concat([train, sex, embark], axis=1)
train.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)

##train.head()
# Everything is numerical, perfect for machine learning

train.drop(['PassengerId'], axis=1, inplace=True)
X = train.drop('Survived', axis=1)
y = train['Survived']

'''

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=101)
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, predictions)

'''

