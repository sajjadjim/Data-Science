import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np
import scipy.stats as stats
# Read the CSV data
data = pd.read_csv("../Assignment 3/Algerian_forest_Modm.csv")
# Select a random sample of size 180 with seed value 5364
sample_data = data['Ws'].sample(n=180, random_state=5364)

# d) Report five summary measures and construct a box plot
summary_measures = {
 'Minimum': np.min(sample_data),
 '1st Quartile (Q1)': np.percentile(sample_data, 25),
 'Median': np.median(sample_data),
 '3rd Quartile (Q3)': np.percentile(sample_data, 75),
 'Maximum': np.max(sample_data)
}
print("\nSummary Measures:")
for measure, value in summary_measures.items():
 print(f"{measure}: {value}")
plt.boxplot(sample_data)
plt.title('Box Plot of Ws Values')
plt.ylabel('Ws')
plt.show()