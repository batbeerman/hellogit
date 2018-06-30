import numpy as np
from random import *

#Q1
array = np.random.random((10,1))
print("Mean is:",np.average(array))



#Q2
array2 = np.random.random((20,1))
print("Variance :",np.var(array2))
print("Standard deviation :",np.std(array2))



#Q3
x = np.random.random((10,20))
y = np.random.random((20,25))
z=np.dot(x,y)
print(z)
print(np.shape(z))
print(np.sum(z))



#Q4
array3 = np.random.random((10,1))
print(array3)
func = 1/(1+np.exp(-array3))
print(func)
