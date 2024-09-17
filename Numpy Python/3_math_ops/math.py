from os import name
import numpy as np

arr1 = np.array([10,20,40])
arr2 = np.array([50,60,60])
arr3 = np.array([2])

## Addition of arrays

# sum = arr1 + arr2
# print(sum)

sum = np.add(arr1,arr2)
print(sum)


## Subtraction of arrays

# sub = arr2 - arr1
# print(sub)

sub = np.subtract(arr2,arr1)
print(sub)


## Multiplication of arrays

# mul = arr1 * arr2
# print(mul)

mul = np.multiply(arr1,arr2)
print(mul)


## Division of arrays

# divide = arr2 / arr1
# print(divide)

divide = np.divide(arr2,arr1)
print(divide)


## power of arrays

# pow = arr1 ** arr3
# print(pow)

pow = np.power(arr1,arr3)
print(pow)



# Square root of arrays

square = np.sqrt(arr1)

# print(square)
print(square.astype(int))


