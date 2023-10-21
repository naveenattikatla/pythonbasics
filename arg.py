# Types of arguments in python
# 1.default arguments 
# 2.positional arguments -> function takes values as user passes to it
# 3.key arguments  -> passing values by key names
# 4. arbitary arguments -> using spread operator 
def GetData(name , id , marks = 35):
    print(name , id , marks)

# positional arguments
GetData("Naveen", 7,50)

# key arguments 
GetData(name = 'Praveen',marks = 90 , id = 12)

# default arguments
GetData("Sai kumar", 13)
print("")

# Use of spread operator

def Sum( a, b, c,d):
    print( a, b, c,d)
input = [ 1 , 4, 2 , 90]
Sum(*input) # spread operator

values = [ { 'id' : 1 , 'Name' : "Naveen",'marks' : 20},{ 'id' : 2, 'Name' : "praveen",'marks' : 50},{ 'id' : 8, 'Name' : "Manoj",'marks' : 10}]

def GetData(a , b ,c):
    print(a , b ,c)

GetData(*values)

def add(*numbers):
    sum = 0 
    for i in numbers:
        sum += i
    return sum

print("Sum is ",add(1,2,3,4,5))

print("")

# sperad operator  withs objects
output = [ *values]
obj = { 'name' : "Bhema", 'marks' : 12,'id' : 1}
