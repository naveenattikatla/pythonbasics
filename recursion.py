def fact(num):
    
    if(num == 1):
        return 1
    return num * fact(num -1)

print("factorial is ", fact(int(input())))

# reverse of a number

num =  int(input())

def reverse(n , rev):

    if( n // 10 == 0):
        return rev * 10 + n
    rev = rev * 10 + (n % 10)
    return reverse(n // 10 , rev)
print(reverse(num , 0 ))