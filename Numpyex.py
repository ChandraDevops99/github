import numpy as np

# Define matrices
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

# Print matrices
print("Matrix 1:")
print(mat1)
print("Matrix 2:")
print(mat2)

# Matrix multiplication
mat = np.dot(mat1, mat2)
print("Matrix multiplication result:")
print(mat)

# Define array
arr = np.array([4, 6, 8, 10])

# Calculate mean value
mean_val = np.mean(arr)
print("Mean value of the array:")
print(mean_val)

#reshape of the array
print('reshape of the array')
arr=np.array([1,2,3])
reshapearr=arr.reshape((3,1))
print(reshapearr)

#flatten function
hello=arr.flatten()
print(hello)

#unique values print
array1=np.array([1,2,3,4,5,6,1,2,3,2,3,2,2])
print("Before Aray values",array1)
print('print unique values' , np.unique(array1))