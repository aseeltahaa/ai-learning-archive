import numpy as np

# 1D
np1 = np.array([1, 2, 3,4,5,6,7,8,9])
for x in np1:
  print(x, end=" ")
print()

# 2D
np2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Individual rows: ")
for x in np2:
  print(x)
print()

print ("Individual elements: ")
for x in np2:
  for y in x:
    print(y, end=" ")
  print()
print()

# 3D
np3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np3:
  for y in x:
    for j in y:
      print(j, end=" ")
print()

# alternative notion
for x in np.nditer(np3):
  print(x, end=" ")
