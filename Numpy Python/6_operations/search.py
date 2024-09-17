import numpy as np

# For Unsorted
arr = np.array([1,2,3,6,8])

s = np.where(arr == 3)
print(s)


# For Sorted
arr1 = np.array([1,2,3,4,5])

ss = np.searchsorted(arr1, 2)
print(ss)
