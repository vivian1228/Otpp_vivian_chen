import numpy as np
import pandas as pd
import yfinance as yf

# Download data
data = yf.download(['^GSPC', 'USDCAD=X'], start="2019-12-31", end="2023-12-31")['Adj Close']

# Preprocess by standardizing
standardized_data = (data - data.mean()) / data.std()

# Desired correlation matrix and its Cholesky decomposition
rho = 0.5  # target correlation
correlation_matrix = np.array([[1, rho], [rho, 1]])
cholesky_decomp = np.linalg.cholesky(correlation_matrix)

# Apply the Cholesky decomposition to adjust correlation
transformed_data = np.dot(standardized_data.fillna(0), cholesky_decomp)

# Convert back to DataFrame and apply original statistics
final_data = pd.DataFrame(transformed_data, columns=data.columns, index=data.index)
final_data = final_data * data.std() + data.mean()

# Verify the new correlation
print(final_data.corr())
