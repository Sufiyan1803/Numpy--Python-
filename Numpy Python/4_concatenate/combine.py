# Concatenate (Joining two arrays)
import numpy as np


print("Combining Arrays")
arr1 = np.array([[1,2,3], [5,6,7]])
arr2 = np.array([[5,4,6], [1,2,3]])

combine = np.concatenate([arr1,arr2])
print("\n Combining the given two arrays: ")
print(combine)




# Combines the given two arrays by taking array values in Vertical way
combine_on_x_axis = np.concatenate([arr1,arr2], axis = 1)
print("\n Combining the given two arrays by taking array values in Vertical way: ")
print(combine_on_x_axis)
 
 
      # Different way
horizontal = np.hstack([arr1,arr2])
print(horizontal)







# Combines the given two arrays by taking array values in Horizontal way
combine_on_y_axis = np.concatenate([arr1,arr2], axis = 0)
print("\n Combining the given two arrays by taking array values in Horizontal way: ")
print(combine_on_y_axis)

       # Different way
vertical = np.vstack([arr1,arr2])
print(vertical)








