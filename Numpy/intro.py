import numpy as np

'''

Numpy arrays are similar to python lists, but they offer several advantages:
1. Performance: Numpy arrays are more efficient for numerical computations.
2. Functionality: Numpy provides a wide range of mathematical functions that operate on arrays.
3. Memory Efficiency: Numpy arrays use less memory compared to python lists for large datasets. 

'''

# Explicit
np1 = np.array([0, 1, 2, 3, 4, 5,])
print("Numpy Array:", np1)
print("Shape: ", np1.shape)

# Range
np2 = np.arange(10)
print("Numpy Array using arange:", np2)

# Step
np3 = np.arange(0, 10, 2)
print("Numpy array using arange with step:", np3)

# Zeros
np4 = np.zeros(10)
print(np4)

# Multidimensional zeros
np5 = np.zeros((3, 4))
print("Multidimensional Zeros Array:\n", np5)

# Ones
np6 = np.ones((2, 3))
print("Ones Array:\n", np6)

# Custom Fill
np7 = np.full(2, 7)
print("Custom Fill Array:\n", np7)

# Another example
np8 = np.full((3, 3), 9)
print("Another Custom Fill Array:\n", np8)

# Convert numpy list to numpy array
my_list = [10, 20, 30, 40]
np9 = np.array(my_list)
print("Converted Numpy Array from list:", np9)