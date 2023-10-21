# Zero by division error
try:
    a , b = map(int , input().split())
    print(a/b)
except ZeroDivisionError as e :
    print("Error" , e )
finally :
    print('Mission completed')


# Index out of bound exception

values = [1 , 2 ,3 ,4]

try:
    print(values[int(input())])
except IndexError as e:
    print(e)
except Exception as e:
    print(e)