import pandas as pd
import scipy.stats as stats
# Read the CSV data
data = pd.read_csv("../Assignment 3/Algerian_forest_Modm.csv")
# Select a random sample of size 180 with seed value 5364
sample_data = data['Ws'].sample(n=180, random_state=5364)

# f) Determine the coefficient of skewness and kurtosis
skewness = stats.skew(sample_data)
kurtosis = stats.kurtosis(sample_data)
print("\nSkewness:", skewness)
print("Kurtosis:", kurtosis)