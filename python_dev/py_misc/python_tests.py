import os, sys

f = open("Macbook.txt", "w")

countThis = 0
for i in range (1,5):
    countThis += 1


f.write("There are " + str(countThis) + " results based on your criteria." )

f.close()
