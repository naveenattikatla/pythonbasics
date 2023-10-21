n = int(input())
k = 1 
for i in range(1, n+1):
    for j in range(1, i+1):
        print(k,end=" ")
       
    print("")
print("")

# Upper One
for i in range(1 , n+1):
    spaces = 0
    for j in range( 1 , n+1):
        if(spaces  == i - 1 ):
            print("1",end=" ")
        else:
            print(end="  ")
            spaces +=1
    print("")

print("")


k = 1
# Opposite Side   
for i in range(1 , n+1):
    spaces  = 0 
    for j in range( 1 , n+1):
        if( n - i == spaces):
            print(k , end= " ")
            
        else:
            print(end="  ")
            spaces +=1
    print("")
print("")
# Pyramid
k = 1
for i in range(1 , n+1):
    spaces  = 0 
    for j in range( 1 , n+1):
        if( n - i == spaces):
            print(k , end= " ")
           
        else:
            print(end=" ")
            spaces +=1
    print("")

print("")
# Diagnols

for i in range(n):
    for j in range(n):
        if(i == j ):
            print("1",end=" ")
        else:
            print(end="  ")
    print("")
