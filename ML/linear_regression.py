# Regression
# The term regression is used when you try to find the relationship between variables.

# In Machine Learning, and in statistical modeling, that relationship is used to predict 
# the outcome of future events.

# Linear Regression
# Linear regression uses the relationship between the data-points to draw a straight line 
# through all them. This line can be used to predict future values.

import numpy as np
from scipy import stats 
import  matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept


plt.scatter(x, y)
plt.plot(x, list(map(myfunc, x))) # Linear regression
plt.show()

