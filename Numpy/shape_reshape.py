import numpy as np

# Sample 1D Array
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Original Array:", np1)
print("Original Array Shape: ", np1.shape)

# Sample 2D array
np2 = np.array([[1,2,3,4, 5,6], [7,8,9,10,11,12]])
print("2D Array:\n", np2)
print(np2.shape) # rows, cols

# Reshape 1D
np3 = np1.reshape(3,4)
print("Reshaped 2D Array (3x4):\n", np3)
print(np3.shape)

# Reshape 2D
np4 = np2.reshape(4,3)
print("Reshaped 2D Array (4x3):\n", np4)
print(np4.shape)

# Flatten 2D array
np5 = np2.reshape(-1)
print("Flattened Array from 2D:\n", np5)