#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 14:18:00 2016
Daniel Billmann, future data scientist
Data Science from Scratch, intro section recreated. 
"""
from __future__ import division
from collections import Counter
users = [
         {"id": 0,"name": "Caesar"},
         {"id": 1,"name": "Victor"},
         {"id": 2,"name": "John"},
         {"id": 3,"name": "Gary"},
         {"id": 4,"name": "David"},
         {"id": 5,"name": "Marco"},
         {"id": 6,"name": "Nemanja"},
         {"id": 7,"name": "Cesc"},
         {"id": 8,"name": "Eden"},
         {"id": 9,"name": "Diego"}
        ]
friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

for user in users:
    user["friends"] = []
#
for i,j in friendships: 
    users[i]['friends'].append(users[j]) #users[i] = user, user['friends'].append(new friend, user J)
    users[j]['friends'].append(users[i])

#how many friends does a user have? 
def num_friends(user):
    return len(user['friends'])
    
total_connections = sum(num_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users
#print(avg_connections)

# sort from "most friends" to "least friends"
#create list of (user_ids, # friends)
num_friends_by_id = [(user['id'], num_friends(user))
for user in users]
#then sort the list
'''
#needs work, list not sorting and 'key=lambda(user_id, num_friends): num_friends, reverse=True' 
#is not working
sorted(num_friends_by_id, key=lambda num_friends: num_friends, reverse=True)
'''

#Data Scientists you may know
def friends_of_friend_ids_bad(user):
    #foaf is short for 'friend of a friend'
    return[foaf['id']
           for friend in user['friends']
           for foaf in friend['friends']
]

# two users not the same if they have different ids
def not_same(user, other_user):
    return[user['id'] != other_user['id']]

#other_user is not a friend of user if other_user is not in user's friends
#returns True or False
def not_friends(user, other_user):
    return all(not_same(user, other_user)
    for friend in user['friends'])
    
def friends_of_friend_id(user):
    return Counter(foaf['id']         
    for friend in user['friends']   # for each of my friends
    for foaf in friend['friends']   # count their friends
    if not_same(user, foaf)         # who aren't me
    and not_friends(user, foaf))    # and aren't my friends
