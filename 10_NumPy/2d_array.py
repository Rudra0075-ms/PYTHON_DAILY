import numpy as np
## 2 d array
arr2=np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr2)
print(arr2.shape)
print(arr2.reshape(1,10))
print(np.arange(0,10,2).reshape(5,1))
print(np.ones((3,4)))   
print(np.eye(3))
