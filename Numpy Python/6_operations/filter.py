import numpy as np

arr = np.array([1,3,4,6])

f_arr = [True,False,False,True]

new_arr = arr[f_arr]


print(new_arr)


print()


f_arr1 = arr>3
new_arr1 = arr[f_arr1]
print(new_arr1)

print()

f_arr2 = arr%2 == 0
new_arr2 = arr[f_arr2]
print(new_arr2)
