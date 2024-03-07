import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV data
data = pd.read_csv("Algerian_forest_Modm.csv")
# Select a random sample of size 180 with seed value 5364
sample_data = data['Ws'].sample(n=180, random_state=5364)

# b) Construct a histogram
plt.figure(figsize=(10, 6))
plt.hist(sample_data, bins=20, edgecolor='black')
plt.title('Histogram of Ws Values')
plt.xlabel('Ws')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()