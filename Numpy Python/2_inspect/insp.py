import numpy as np
from regex import P

a = np.array([[10,20,30],[40,50,60],[70,80,90]])


# to find shape of array (rows, columns)
shape = np.shape(a)
print("Shape of array is in form (rows,columns): ",shape)

# to find size of array
size = np.size(a)
print("Size of array is: ",size)

# to find dimension of array
dimension = np.ndim(a)
print("Array is of",dimension,"D","dimension")

# to find datatype stored in array
datatype = a.dtype
print("DataType of Array is: ",datatype)

# to find length of array
length = len(a)
print("Length of array is: ",length)

# to convert array to different datatype
diff_datatype = a.astype(str)
print(diff_datatype)
