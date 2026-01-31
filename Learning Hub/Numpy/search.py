import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9,10])
print("Array np1: ")
print(np1)
print("Indeces where np1 is 3: ")
print(np.where(np1 == 3))

print("Indeces where np1 is greater than 5: ")
print(np.where(np1 > 5))

print("Indeces where np1 is even: ")
print(np.where(np1 % 2 == 0))