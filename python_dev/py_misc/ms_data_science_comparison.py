# -*- coding: utf-8 -*-
import csv
ms_school = {}
ms_schools = {}
addSchool = True
while addSchool == True:
    newSchool = input("Would you like to enter a school? Please enter 'yes' or no: ").lower()
    # need to add "convenient class times"
    # need to add length of program
    if newSchool == "yes":
        school_name = input("What is the school's name? ")
        cost = input("What is the total cost of the program? ")
        cost_impact= 0
        skills = input("How compatible are the technical aspects with what you want to learn? Please use a scale from 1-10: ")
        feel = input("How compatible are the intangible aspects of the school? Please use a scale from 1-10: ")
        geo = input("How compatible are the geographic aspects with what you want to learn? Please use a scale from 1-10: ")
        full_time = input("How strong are the full-time opportunities after this program? Please use a scale from 1-10: ")
        program_length = input("How long is the program (in months)? ")
        cs = input("Does it require a computer science background? ").lower()
        stats = input("Does it require a statistics background? ").lower()
        eng = input("Does it require an engineering background? ").lower()
        classes = input("How many prerequisite classes will you need to take? ")
        prereqs = 0
        length_rating = 0
        overall_rating = 0
        done = True
        while done == True:
            try:
                cost = float(cost)
                if cost > 100000:
                    cost_impact = 10
                elif cost > 80000:
                    cost_impact = 7
                elif cost > 60000:
                    cost_impact = 5
                elif cost > 40000:
                    cost_impact = 3
                else: 
                    cost_impact = 1
                done = False
            except: 
                print("That is not a number!")
        while done == False: 
            try:
                skills = int(skills)
                if skills<=10:
                    done = True
                else:
                    print("Please enter an integer from 0 to 10: ")
            except:
                print("Please enter an integer from 0 to 10: ")
        while done == True: 
            try:
                feel = int(feel)
                if feel<=10:
                    done = False
                else:
                    print("Please enter an integer from 0 to 10: ")
            except:
                print("Please enter an integer from 0 to 10: ")
        while done == False:
            try:
                geo = int(geo)
                if geo<=10:
                    done = True
                else:
                    print("Please enter an integer from 0 to 10: ")
            except:
                print("Please enter an integer from 0 to 10: ")
        while done == True:
            try:
                full_time = int(full_time)
                if full_time<=10:
                    done = False
                else:
                    print("Please enter an integer from 0 to 10: ")
            except:
                print("Please enter an integer from 0 to 10: ")
        
        #length of program
        done = True
        try:
            while done == True: 
                program_length = int(program_length)   
                if program_length > 36:
                   done = False
                   length_rating = 1
                elif program_length > 30: 
                    done = False
                    length_rating = 3
                elif program_length > 24: 
                    done = False
                    length_rating = 6
                elif program_length > 18:
                    done = False
                    length_rating = 7
                else:
                    done = False
                    length_rating = 10
        except:
            print('please enter a number: ')
        #prerequisites
        try:
            while done == False:
                if cs == 'yes':
                    done = True
                    prereqs += 2
                elif cs == 'no':
                    done = True
                    prereqs += 8
                else:
                    print('Please enter \'yes\' or \'no\': ')
        except:
            print('Please enter \'yes\' or \'no\': ')
        try:
            while done == True:
                if stats == 'yes':
                    done = False
                    prereqs += 3
                elif stats == 'no':
                    done = False
                    prereqs += 7
                else:
                    print('Please enter \'yes\' or \'no\': ')
        except:
            print('Please enter \'yes\' or \'no\': ')    
        try:
            while done == False:
                if eng == 'yes':
                    done = True
                    prereqs += 1
                elif eng == 'no':
                    done = True
                    prereqs += 9
                else:
                    print('Please enter \'yes\' or \'no\': ')
        except:
            print('Please enter \'yes\' or \'no\': ')
        done = True
        while done == True:
            classes = int(classes)
            if classes < 2:
                done = False
                prereqs += 9                
            elif classes < 4:
                done = False
                prereqs += 7                
            elif classes < 6:
                done = False
                prereqs += 4
            elif classes < 8:
                done = False
                prereqs += 2
            if classes > 8:
                done = False
                prereqs += 0
            else:
                print('Please enter a number between 0 and 10')
       
        ms_school['Overall Rating'] = overall_rating
        ms_school['school_name'] = school_name
        ms_school['cost impact'] = cost_impact
        ms_school['Technical Compatibility']= skills
        ms_school['\'Feel Impact\''] = feel
        ms_school['Geographic Interest'] = geo
        ms_school['Full-time opportunities'] = full_time
        ms_school['International Students'] = program_length
        ms_school['Computer Science requirement?'] = cs
        ms_school['Statistics background requirement?'] = stats
        ms_school['Engineering background requirement?'] = eng
        ms_school['Number of prerequisite classes'] = classes
        overall_rating = cost_impact + skills + feel + geo + full_time + length_rating + prereqs
        ms_schools[ms_school['school_name']] = overall_rating
        with open('masters.csv', 'a', newline='') as masters:
            writer = csv.writer(masters, delimiter=' ')
            for key, value in ms_schools.items():
                writer.writerow([key, value])
        print("Thank you, your response has been recorded.\n")
    elif newSchool == "no":
        addSchool = False
        print("We will compare the current schools at this time.")
        #add function to return the best school/program to the user
        for key, value in ms_schools.items():
            if value == max(ms_schools.items()):
                print("\n" + key + " is the best school for you with a rating of " + value + ".")
    else:
        print("Please enter 'yes' or 'no'")       