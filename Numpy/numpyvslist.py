import sys
import numpy as np
import time
l1=[i for i in range(1, 200000)]
l2=[i for i in range(1, 200000)]
a1= np.arange(1,200000)
a2= np.arange(1,200000)

# Fast

start = time.time()
result = a1+a2
print("numpy tool",(time.time() - start )*1000)

start = time.time()
result = [ (x+y)  for x,y in zip(l1,l2) ]
print("list took",(time.time() - start  ) * 1000)

# Less Memory

List = [1,2,4,5]
print(sys.getsizeof(3) * len(List))


Values =np.array([1,2,3,4])
print(Values.size * Values.itemsize)
