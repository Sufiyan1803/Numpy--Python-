import numpy as np


arr = np.array([1,2,3,4,5,6])

# Append adds value at last index
add_on_last = np.append(arr,[7])  
                      #(arr,value)           
print(add_on_last)


# Insert value as per given index
insert = np.insert(arr,1,[0])
              #(arr,index,value)
print(insert)


# Delete value as per given index
delete = np.delete(arr,1)
                #(arr,index)
print(delete)


