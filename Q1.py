#the following code is used to generate a time series based on 2 i.i.d. time series which are distributied
#as N(0,1)
#user formula Y = rho * X + np.sqrt(1 - rho**2) * Z


import numpy as np

# Set the seed for reproducibility
np.random.seed(0)

# Define the sample size
n = 5000

# Define the correlation coefficient
rho = 0.5  # Example correlation

# Generate X as a standard normal variable
X = np.random.normal(0, 1, n)

# Generate Z as an independent standard normal variable
Z = np.random.normal(0, 1, n)

# Generate Y using the formula for a correlated normal variable
Y = rho * X + np.sqrt(1 - rho**2) * Z

# Check the correlation
actual_rho = np.corrcoef(X, Y)[0, 1]
print("Theoretical rho: ", rho)
print("Actual rho from generated data: ", actual_rho)