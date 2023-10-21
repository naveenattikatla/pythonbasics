# closure forms a bundle with its lexical envirnment , simple speaking function + its lexical envirnment
def Outer():
    a  = 10 
    def inner():
        print(a)
    return inner

# Outer()()
#  implement own filter method

def filter(fun , values):
    output = [ ]
    for i in values:
        if(fun(i)):
            output.append(i)
    return output

# print(filter(lambda x : x % 2 == 0 , [ 1 , 3,2,5,4]))
# function curring
def add(num):
    def inner(num1 = None ):
        if(num1 == None):
            return num
        return add( num + num1)
    return inner
result = add(1)(3)(45)()

# print(result)

def sum(a , b=9, c=0,d=0):
    return a +b + c+ d


# implementing own curring in python

def Summation(fun):
    def inner(*num):
        if(len(num) >= fun.__code__.co_argcount): 
           return  fun(*num)
        else:
            return lambda next :  inner(*num , next)
         
    return inner

Addition = Summation(sum)

output =Addition(11)(300)(31)(3)
print(output)

