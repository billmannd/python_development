# -*- coding: utf-8 -*-

# program that allows you to create a .json file of contact information for 
# a person you create in the database.
import os
import glob
currDir = "/Users/danielbillmann/python_development/python_dev/py_misc"
jsonDir = "/Users/danielbillmann/python_development/python_dev/py_misc/JSON_contacts"

# build a dictionary to host the information 
contact_list = {}

done = True
while done == True:
    addFriend = input("Would you like to add a new friend to your contact list? Please type 'yes' or 'no': ")
    addFriend.lower()
    print(addFriend)
    if addFriend == "yes": 
        #create a new friend
        firstName = input("What is your first name? ")
        lastName = input("What is your last name? ")
        lastSchool = input("What is the last school you attended? ")
        phone = input("What is your phone number? Please leave out spaces or hyphens: ")
        street = input("What is your street address? ")
        city = input("What city do you live in? ")
        state = input("Which state is that city in? " ) 
        zipCode = input("What is your zip code? " )
        friend = {'firstName': firstName, 'lastName':lastName, 'lastSchool':lastSchool ,'phone': phone, 'address': {'street': street, 'city': city, 'state': state, 'zipCode': zipCode}}        
        new = str(firstName + "_" + lastName + '.json')
        if os.path.isfile(new):
            done = False
            print("File already exists")
        else: 
            with open(new, 'w') as new:
                for key in friend: 
                    new.write(str(key) + ":" + str(friend[key]) + "\n")
                new.close()
        contact_list.update({friend['firstName']: friend})     
        print(contact_list)        
    elif addFriend == "no": 
        done = False
        print("It's ok to not have any friends.")
    else:
        print("Invalid input, please try again")
        addFriend = input("Would you like to add a new friend to your contact list? Please type 'yes' or 'no' ").lower()
json = glob.glob("*.json")
for i in json:
    if json:
        os.rename(currDir + "/" + i, jsonDir + "/" + i)