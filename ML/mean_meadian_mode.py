array =  [64, 34, 25, 12, 22, 11, 90, 5, 34, 64, 22, 22]

import numpy as np
from scipy import stats

print(f"Mean Value: {np.mean(array)}")
print(f"Median Value: {np.median(array)}")

mode_result = stats.mode(array)
print(f"Mode Value: {mode_result.mode}")
print(f"Mode count: {mode_result.count}")

