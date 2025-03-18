#Standard deviation is a number that describes how spread out the values are.

#A low standard deviation means that most of the numbers are close to the mean (average) value.

#A high standard deviation means that the values are spread out over a wider range.

#Standard Deviation is often represented by the symbol Sigma: σ

#Variance is often represented by the symbol Sigma Squared: σ2

import numpy as np

speed = [86,87,88,86,87,85,86]

print(f"standard deviation: {np.std(speed)}")

speed = [32,111,138,28,59,77,97]

print(f"standard deviation: {np.std(speed)}")

#Variance
# 
# Variance is another number that indicates how spread out the values are.

print(f"variance: {np.var(speed)}")
 