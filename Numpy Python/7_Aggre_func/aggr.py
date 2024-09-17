import numpy as np

arr = np.array([1,2,3,4,5])

# Aggregations Functions

print("AGGREGATION FUNCTIONS: ")
print()
sum = np.sum(arr)
print(sum)

min = np.min(arr)
print(min)

max = np.max(arr)
print(max)

prod = np.prod(arr)
print(prod)

mean = np.mean(arr)
print(mean)

cumsum = np.cumsum(arr)
print(cumsum)

cumprod = np.cumprod(arr)
print(cumprod)
print()

# 2D data with the help of example

print("2D Data example: ")
print()
a = [10,20,30,40,50,60]
b = [2,4,6,8,10,12]

price = np.array(a)
quantity = np.array(b)

print(price, quantity)
print()

cprod = np.cumprod([price,quantity], axis=0)
ncprod = cprod[1]
print(ncprod)
print()

# Total = np.sum(ncprod)
# print(Total)
print(ncprod.sum())
