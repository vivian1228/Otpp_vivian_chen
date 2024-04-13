
import numpy as np

# Set the seed
np.random.seed(0)

# sample size
n = 5000

# Define the correlation coefficient
rho = 0.5

# Generate X as a standard normal variable
X = np.random.normal(0, 1, n)

# Generate Z as an independent standard normal variable
Y = np.random.normal(0, 1, n)

# Generate Y using the formula for a correlated normal variable
Z = rho * X + np.sqrt(1 - rho**2) * Y

# Check the correlation
actual_rho = np.corrcoef(X, Z)[0, 1]
print("Theoretical rho: ", rho)
print("Actual rho between X and Z: ", actual_rho)