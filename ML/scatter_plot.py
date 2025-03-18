import numpy as np
import matplotlib.pyplot as plt 

#200 random values between 10 and 100 
x_values = np.random.uniform(10, 100, 200)
y_values = np.random.uniform(10, 100, 200)

plt.scatter(x_values, y_values)
plt.show()

#200 normal distribution values between 10 and 100 
x_values = np.random.normal(10.0, 1.0, 200)
y_values = np.random.normal(5.0, 2.0, 200)

plt.scatter(x_values, y_values)
plt.show()