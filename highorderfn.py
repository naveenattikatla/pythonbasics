from functools import reduce # to import reduce function 
 
values = [ { 'id' : 1 , 'Name' : "Naveen",'marks' : 20},{ 'id' : 2, 'Name' : "praveen",'marks' : 50},{ 'id' : 8, 'Name' : "Manoj",'marks' : 10},
{'id ' : 3 ,'Name' : "sai",'marks' : 40},{ 'id' : 4 , 'Name' : "Ashwin",'marks' : 90},{'id' : 5 , 'Name' : "Murali",'marks' : 85}]

# returing values whose marks are greater than 35

def Toppers(data):
    return data['marks'] >= 35

output = list(filter(Toppers , values))
print("Toppers are here",output)

# Assiging Marks sheet for whose people who scored 50 + marks

print("")
def Add_School(value):
    value['School Name'] = "Zph high"
    return value 

output = list(map(Add_School , values))
print("School Names are added",output)

print("")

# Finding Total marks of student to just demanstrate about how does reduce works 

def GetValues(data , data1 ):
    return data + data1['marks'] 
output = reduce(GetValues, values ,0)
print(output)

 

