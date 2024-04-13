import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.preprocessing import StandardScaler
import numpy as np
scaler = StandardScaler()

# fetch dataset
wine = fetch_ucirepo(id=109)

# data (as pandas dataframes)
X = wine.data.features
X = X.dropna()
# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the data
normalized_data = scaler.fit_transform(X)

df=pd.DataFrame(normalized_data)
print(df.describe())