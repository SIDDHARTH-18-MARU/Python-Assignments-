import numpy as np

# 1. Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# 2. Create a 2D array
arr2 = np.array([[1, 2], [3, 4]])
print("2D Array:\n", arr2)

# 3. Generate an array of zeros
zeros_arr = np.zeros((2, 3))
print("Array of Zeros:\n", zeros_arr)

# 4. Generate an array of ones
ones_arr = np.ones((3, 2))
print("Array of Ones:\n", ones_arr)

# 5. Generate an identity matrix
identity = np.eye(3)
print("Identity Matrix:\n", identity)

# 6. Generate a range of numbers
range_arr = np.arange(10)
print("Range Array:", range_arr)

# 7. Reshape an array
reshaped = np.arange(12).reshape(3, 4)
print("Reshaped Array (3x4):\n", reshaped)

# 8. Transpose a matrix
transposed = arr2.T
print("Transposed Array:\n", transposed)

# 9. Add two arrays
sum_arr = arr1 + np.array([5, 4, 3, 2, 1])
print("Sum of Arrays:", sum_arr)

# 10. Multiply arrays element-wise
product = arr1 * 2
print("Element-wise Multiplication:", product)

# 11. Matrix multiplication
matmul = np.dot([[1, 2], [3, 4]], [[5, 6], [7, 8]])
print("Matrix Multiplication:\n", matmul)

# 12. Find maximum and minimum
max_val = arr1.max()
min_val = arr1.min()
print("Maximum:", max_val)
print("Minimum:", min_val)

# 13. Find mean and standard deviation
mean_val = arr1.mean()
std_dev = arr1.std()
print("Mean:", mean_val)
print("Standard Deviation:", std_dev)

# 14. Sort an array
sorted_arr = np.sort(np.array([3, 1, 4, 2]))
print("Sorted Array:", sorted_arr)

# 15. Flatten a multi-dimensional array
flattened = arr2.flatten()
print("Flattened Array:", flattened)
