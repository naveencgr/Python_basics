# In the real world, the data sets are much bigger, but it can be difficult to 
# gather real world data, at least at an early stage of a project.

import numpy as np
import matplotlib.pyplot as plt 
random_values = np.random.uniform(0.0, 10.0, 250)

print(random_values)

plt.hist(random_values, 10)
plt.show()

#you can also generate random values of any size

#np_values = np.random.uniform(0.0, 100.0, 1000000)
# plt.hist(np_values, 1000)
# plt.show()
