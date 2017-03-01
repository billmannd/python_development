# Dan Billmann's demonstration of file mastery
import os
import pandas


# 1. use a for loop to creat n text files
folderPath = "/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/file_work"
originFile = "/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/Space-Separated.txt"
for i in range(0, 5):
    fileI = "file" + str(i) + ".txt"
    #print(fileI)
# 2. convert text files to csv files
    fileI = os.path.splitext(fileI)[0]
    fileI = "/" + str(fileI) + ".csv"
    fileI = folderPath + fileI
# 3. write in the data from 
# "/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/Space-Separated.txt"
# into each file
    with open(fileI, "w+") as file:
        with open(originFile, "r+") as o:
            for line in o:
                file.write(line)
'''
f0 = pandas.read_csv(folderPath + "/file0.csv", ' ')
f0 = pandas.read_excel(folderPath + "/file0.csv", ' ')
#filez = "/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/Boulder2016.xlsx"
#ex1 = pandas.read_excel(filez, sheetname="Boulder")

rfile = "/Users/danielbillmann/Dropbox/1.xlsx"
blue = pandas.read_excel(rfile, spreadsheet="Sheet1")
'''
# 4. call a panda on one of the files
# 5. work with excel_ouput 