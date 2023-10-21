file = open("file.txt",'r') # reading text 
output = file.readline()
file.close()

file  = open("file.txt" ,'w') # writing context to file
file.write("good to be here")

file  = open("file.txt" ,'a') # appending data
file.write(" Next Line to discuss ")
file.close()

# print(open("file.txt",'r').readline())
file.close()

# with help of with clause

with open("file.txt",'a') as file:
    file.write("This is how files works in python")

with open("file.txt",'r') as file:
    output = file.readline()
    print(output)