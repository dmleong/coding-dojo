import numpy as np


a = np.array([2,3,1,0])
b = np.array((2, 3, 1, 0))
c = np.array([[1,2.0],[0,0],(1+1.j,3.j)])     # note mix of types: tuple and lists
d = np.array([[ 1.+0.j, 2.+0.j], [ 0.+0.j, 0.+0.j], [ 1.+1.j, 3.j]])

print a
print b
print c
print d
