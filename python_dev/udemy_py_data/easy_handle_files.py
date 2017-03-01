filename = "/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/newTest.txt"
dirpath = "/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/dirPath.txt"
"""
file =open(filename, 'w') 
file.close()

with open(filename, 'w') as file: 
    file.write("This is a python test")
"""

with open(dirpath, 'a') as direct: 
    direct.write("\nHopefully it's worth it")

#file.close()
direct.close()