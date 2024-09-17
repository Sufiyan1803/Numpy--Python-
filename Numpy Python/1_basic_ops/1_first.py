import numpy as np

# Basic array
a = np.array([10,20,30])
b = np.array([40,50,60])

print(a+b)

l  = [10,20,30]
print(l)

# array of zeros
print(np.zeros(5))

print(np.zeros((2,3)))


# array of ones
print(np.ones(5))

print(np.ones((2,3)))


# array of random
print(np.random.rand(5))

# array of choice
print(np.full((2,2),7))


# Imatrix (Identity matrix)
print(np.eye(3))