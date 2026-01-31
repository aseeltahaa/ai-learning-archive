import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9])
print(np)
x = [True, False, True, False, True, False, True, False, True]
print(np1[x])
 
# Custom filtering
filtered_list = []
for thing in np1:
    if thing % 2 == 0:
        filtered_list.append(True)
    else:
        filtered_list.append(False)

print(np1[filtered_list])

# Shortcuts
filter = np1 % 2 == 0
print(np1[filter])