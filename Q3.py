import numpy as np
import pandas as pd

# Define a 4x4 correlation matrix R
R = np.array([
    [1.0, 0.5, 0.3, 0.1],
    [0.5, 1.0, 0.4, 0.2],
    [0.3, 0.4, 1.0, 0.5],
    [0.1, 0.2, 0.5, 1.0]
])

# Perform Cholesky decomposition
L = np.linalg.cholesky(R)

# Generate 4 independent N(0,1) series(size = 1000)
np.random.seed(0)  # For reproducibility
Z = np.random.normal(0, 1, (1000, 4))

# Apply the Cholesky matrix to generate correlated series
X = np.dot(Z, L.T)

# Convert to DataFrame for nicer output and possible further analysis
df = pd.DataFrame(X, columns=['Series_1', 'Series_2', 'Series_3', 'Series_4'])

# Verify the resulting correlation matrix matches R
resulting_correlation_matrix = df.corr()
print(resulting_correlation_matrix)