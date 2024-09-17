
OVERVIEW:



numpy.append()

The append() method allows you to concatenate two or more arrays along a specified axis. This joins the arrays end-to-end and returns a new array with the combined elements.

      import numpy as np

      arr1 = np.array([1, 2, 3])
      arr2 = np.array([4, 5, 6])

      arr_appended = np.append(arr1, arr2)

      print(arr_appended)
      
# [1 2 3 4 5 6]

-------------------------------------------------

numpy.delete()

The delete() method allows you to remove or delete elements from an array by index position along a specified axis. This modifies the array in-place instead of returning a new array.


      import numpy as np

      arr = np.array([1, 2, 3, 4])

      np.delete(arr, 1)

      print(arr)
# [1 3 4]

-------------------------------------------------

numpy.insert()

The insert() method allows you to insert elements into an array at a given index position along a specified axis. This also modifies the original array in-place.


      import numpy as np

      arr = np.array([1, 2, 4, 5])

      np.insert(arr, 2, 3)

      print(arr)
# [1 2 3 4 5]

--------------------------------------------------

Now let’s explore the full syntax, parameters, and examples of using these functions for modifying NumPy arrays.

numpy.append() Detail and Examples

The full syntax for numpy.append() is:

numpy.append(arr, values, axis=None)

Where:

arr is the array you want to append to.
values are the array or value(s) you want to append.
axis (optional) is the axis along which you want to append the values. By default it is None, which appends flattened values to the end of arr.
The return value is a new NumPy array with the concatenated elements.

Let’s look at some examples of appending arrays and values:

     import numpy as np

     arr1 = np.array([1, 2, 3])
     arr2 = np.array([4, 5, 6])

# Append arr2 to arr1
     arr_appended = np.append(arr1, arr2)

     print(arr_appended)
# [1 2 3 4 5 6]

# Append a value to arr1
     arr_appended = np.append(arr1, 100)

     print(arr_appended)
# [  1   2   3 100]

We can also append arrays along an axis. For example, appending rows:

    arr1 = np.array([[1, 2, 3], [4, 5, 6]])

# Append new row
     arr2 = np.array([[7, 8, 9]])

    arr_appended = np.append(arr1, arr2, axis=0)

     print(arr_appended)

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

Appending columns by specifying axis=1:

       arr1 = np.array([[1, 2], [3, 4]])
        arr2 = np.array([[5, 6]])

         arr_appended = np.append(arr1, arr2, axis=1)

        print(arr_appended)

# [[1 2 5 6]
#  [3 4 5 6]]

numpy.delete() Detail and Examples

The full syntax for numpy.delete() is:

numpy.delete(arr, obj, axis=None)

Where:

arr is the array you want to delete from
obj are the indices or slices to delete
axis (optional) is the axis along which to delete elements. By default it is flattened.
Unlike append(), delete() modifies the input array in-place rather than returning a new array.

Let’s go through some examples of deleting by index position or slice:

        import numpy as np

        arr = np.array([1, 2, 3, 4, 5])

# Delete index 1
        np.delete(arr, 1)

        print(arr)
# [1 3 4 5]

        arr = np.array([1, 2, 3, 4, 5])

# Delete slice
       np.delete(arr, [1, 3])

        print(arr)
# [1 3 5]

We can also delete along an axis like rows or columns:

        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Delete second row
       np.delete(arr, 1, axis=0)

# [[1 2 3]
#  [7 8 9]]

# Delete first column
      np.delete(arr, 0, axis=1)

# [[2 3]
#  [5 6]
#  [8 9]]

numpy.insert() Detail and Examples

The full syntax for numpy.insert() is:

numpy.insert(arr, obj, values, axis=None)

Where:

arr is the input array to insert into
obj is the index to insert at
values are the values to insert
axis (optional) is axis along which to insert, default is flattened
The insert() method also modifies the array in-place rather than returning a new array.

Let’s insert some values:

import numpy as np

      arr = np.array([1, 2, 4, 5])

# Insert at index 2
      np.insert(arr, 2, 3)

      print(arr)
# [1 2 3 4 5]

# Insert multiple values
      np.insert(arr, [2, 3], [100, 200])

      print(arr)
# [  1   2 100   3 200   4   5]

We can also insert along an axis like rows or columns:

      arr = np.array([[1, 2], [5, 6]])

# Insert row
      np.insert(arr, 1, [[3, 4]], axis=0)

# [[1 2]
#  [3 4]
#  [5 6]]

# Insert column
      np.insert(arr, 1, [[10], [20]], axis=1)

# [[ 1 10  2]
#  [ 3 20  4]
#  [ 5 20  6]]
