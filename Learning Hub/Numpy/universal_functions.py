import numpy as np

np1 = np.array([-3, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Original Array: \n", np1)

# square root of each element
print("Square root: \n", np.sqrt(np1))

# absolute value
print("Absolute value: \n", np.abs(np1))

# exponential of each element
print("Exponential: \n", np.exp(np1))

# natural logarithm of each element
print("Natural Logarithm: \n", np.log(np1 + 1)) 

# minimum in an array
print("Minimum value: \n", np.min(np1))

# maximum in an array
print("Maximum value: \n", np.max(np1))

# maximum in a slice
print("Maximum in slice [3:9]: \n", np.max(np1[3:9]))

# mean of the array
print("Mean value: \n", np.mean(np1))

# median of the array
print("Median value: \n", np.median(np1))

# standard deviation of the array
print("Standard Deviation: \n", np.std(np1))

# variance of the array
print("Variance: \n", np.var(np1))

# sine of each element (in radians)
print("Sine values: \n", np.sin(np1))

# cosine of each element (in radians)
print("Cosine values: \n", np.cos(np1))

# tangent of each element (in radians)
print("Tangent values: \n", np.tan(np1))