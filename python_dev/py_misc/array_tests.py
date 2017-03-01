stringOut = []
stringOut.append("Sucks")

stringOut[0] = 1
stringOut.append(0)
stringOut.append(1)
stringOut.append(0)

a = [1, 1, 1, 0]
b = [0, 0, 1, 1]
c = [stringOut, a, b]
print(c)

i = 0
while i < len(a):
    z = 0    
    usr_i = input("Would you like to replace a value in the array? Y or N: ")
    usr_i = usr_i.lower()
    print(usr_i)
    if usr_i == "y":
        new_val = input("What new value would you like to add in? ")
        stringOut.insert(z, new_val)
        z+= 1
    i+=1
print(c)