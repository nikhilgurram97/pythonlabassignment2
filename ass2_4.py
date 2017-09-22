import numpy as np
a=np.random.random((15))
print(a)
b=a.max()
print("max is ",b)
np.put(a,b,100)
print(a)
c=a.max()
print("max is" ,c)