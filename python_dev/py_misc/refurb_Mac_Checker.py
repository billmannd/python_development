"""
The below program demonstrates my understanding of the following concepts in Python:
When to use libraries
How to connect to the internet
Reading and writing and files
Loops (do-while, while, for, foreach)
Conditional statements (if-then logic)
running a program from a file
program documentation
"""

import os, sys
import shlex
import urllib.request
with urllib.request.urlopen('http://www.apple.com/shop/browse/home/specialdeals/mac/macbook_pro/15') as response:
   contents = response.read()

output = open('out.txt', 'r+')
output.write(str(contents))


f = open('out.txt', 'r')
t = open('MacBookout.txt', 'r+')
lineCount = 0
returnCount = 0
#Goes over each line in the file
for line in f:
    #counts the line number
    lineCount += 1
    #if 'specs ' is in the line, add 22 and use that as a new range
    if 'specs' in line:
        lineRange = lineCount + 22

    # if the line with specs is in the range,
        for line in range (lineCount, lineRange):
            woo = (f.readline(lineCount))
            if '16GB' in woo:
                returnCount += 1
                print(woo)
    o = open('MacBookout.txt', 'w')
    o.write("There are " + str(returnCount) + " results based on your search.")
    o.close()

f.close()


