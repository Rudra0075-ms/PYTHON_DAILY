import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Array : \n", arr)
print(arr[1:,1:3])
print(arr[0][0])
print(arr[0:2,2:])
print(arr[1:,2:])

arr[0,0]=100
print(arr)

arr[1:]=100
print(arr)
