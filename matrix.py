import numpy as np
a=np.ones((5, 5),dtype=int)
list=[0,1]
i=0
i1=1
for f in range(0,23):
    i1=i1+i
    list.append(i1)
    i=i1-i
a1=np.array(list,dtype=int)
a1.shape=(5,5)
print(a1)
s=sum(a+a1)
