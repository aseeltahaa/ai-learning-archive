import numpy as np

'''

  Slicing is the process of extracting a subset of elements from an array.

'''
print("Slicing 1 Dimensional Arrays")
# Sample array
np1 = np.array([0, 1, 2, 4, 3, 5, 6, 7, 8, 9])
print("Original array:", np1)

# Return 2,4,3,5
print("Sliced array:", np1[2: 6])

# Return 4, till the end
print("Sliced array : ", np1[4:])

# Return beginning to 5
print("Sliced array : ", np1[:6])

# Return the last 2 elements
print("Sliced array : ", np1[-2:])

# Return all elements except the last 2
print("Sliced array: ", np1[:-2])

# Steps
print("All even indeces: ", np1[::2])
print("All odd indeces: ", np1[1::2])
print("Every 3rd item: ", np1[::3])



print("\nSlicing 2 Dimensional Arrays")
# Sample Array
np2 = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])
print("Original array:\n", np2)

# (row, column)

# Return 6,7
print("Slice array 2: ", np2[1, 1:3])
# Return 2nd row
print("Slice array 2: ", np2[1, :])
# Return 1, 2, 6, 7
print("Slice array 2:\n", np2[0:2, 0:2])
# Return every other element
print("Slice array 2:\n", np2[:, ::2])