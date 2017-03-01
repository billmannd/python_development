import os
import re

count = 0
with open("regex_practice.txt", "r") as rxp:
    for line in rxp:
        count+=1
        str(count)
        print(count, line)

        