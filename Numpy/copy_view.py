import numpy as np

'''
  copy() is similar to pass by value -> independent arrays, operations on one do not affect the other
  view() is similar to pass by reference -> any modification in original array will reflect in view array

'''

# Sample Array
np1 = np.array([1, 2, 3,4,5,6,7,8,9,10])
print("Original Array: ", np1)

# View
np2 = np1.view()
print("View of np1 (np2): ", np2)
np1[0] = 100
print("np1 after modifying first element: ", np1)
print("np2 (view of np1) after modifying np1: ", np2)


# Sample array for copy
np3 = np.array([11, 12, 13,14,15,16,17,18,19,20])
print("Original Array for copy: ", np3)

# Copy
np4 = np3.copy()
print("Copy of np3 (np4): ", np4)
np3[0] = 200
print("np3 after modifying first element: ", np3)
print("np4 (copy of np3) after modifying np3: ", np4)