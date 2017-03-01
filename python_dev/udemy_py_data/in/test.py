import os

os.chdir("/Users/danielbillmann/Dropbox/Developing/python_dev/udemy_py_data/in")

#os.rename('test.csv', 'test.txt')

#imports global variable
import glob

rubyList=glob.glob("*.rb")
print(rubyList)

pyList=glob.glob("*.py")
print(pyList)

for i in rubyList: 
	
	filename=os.path.splitext(i)[0]
	
	newname=filename+".py"
	
	os.rename(i, newname)

print(rubyList)