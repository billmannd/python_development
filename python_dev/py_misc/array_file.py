ids=["B3","\nB4","\nB5","\nB6"]

for i in ids: 
    with open("C:\\in\\testing1.txt", 'a') as file:
        file.write(i)

file = open("C:\\in\\testing1.txt", 'r')
print(file.read())