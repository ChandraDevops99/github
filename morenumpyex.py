import numpy as np
import numpy.ma as ma

a = np.array([1, 2, 3, 4, -1])
maska = ma.masked_less(a, 3)
print(maska)

newmask=maska.filled(1)
print(newmask)
a1 =np.array([0,1,2,3,4,5,6,7,8])
b1=np.split(a1,3)
print(b1)