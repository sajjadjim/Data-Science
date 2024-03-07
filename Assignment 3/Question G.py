import pandas as pd
import numpy as np
# Read the CSV data
data = pd.read_csv("../Assignment 3/Algerian_forest_Modm.csv")
# Select a random sample of size 180 with seed value 5364
sample_data = data['Ws'].sample(n=180, random_state=5364)

# g) Determine covariance and correlation matrices
covariance_matrix = np.cov(sample_data)
correlation_matrix = np.corrcoef(sample_data)
print("\nCovariance Matrix:")
print(covariance_matrix)
print("\nCorrelation Matrix:")
print(correlation_matrix)