# Iterators 
def GetValues(values):
    for i in values:
        yield i
output  = GetValues([1,2,3,4])
output = iter(output)

print(output.__next__())
print(output.__next__())
print(output.__next__())
print("")

# Returing mutiple values using iterators

def GetSumandMul(a ,b):
    sum = a + b
    mul = a * b
    for  i in [ sum , mul]:
        yield i 

output = iter(GetSumandMul(3,4))
print(output.__next__())
print(output.__next__())