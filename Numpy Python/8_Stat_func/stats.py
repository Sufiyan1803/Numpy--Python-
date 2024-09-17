import numpy as np
import statistics as stats

arr = np.array([10,20,30,40,20,70,50,60])

# Sum of all values/number of values
print(np.mean(arr))

# Certral value after sorting
print(np.median(arr))

# most reocuured value
print(stats.mode(arr))

# Standard deviation
print(np.std(arr))

# variance (square of standard deviation)
print(np.var(arr))



#Co-relation_Co-efficient (used to compare values to find relation)
# In Output:
# -1 represents inversely proportional relationship
# 1 represents proportional relationship
# 0 means no relationship


# It shows that as per the price increases , sales also increases
Price = [10,50,100,40,20]
sales = [2,7,11,5,3]

c = np.corrcoef([Price,sales])
print(c)



# It shows that as per the price increases , sales decreases
Price1 = [20,10,40,70,90]
sales1 = [7,5,3,2,1]

c1 = np.corrcoef([Price1,sales1])
print(c1)

