import pandas as pd
import statistics
import scipy.stats as stats
# Read the CSV data
data = pd.read_csv("Algerian_forest_Modm.csv")
# Select a random sample of size 180 with seed value 4691
sample_data = data['Ws'].sample(n=180, random_state=5364)


# c) Calculate mean, median, mode, geometric mean, and harmonic mean
mean_Ws = statistics.mean(sample_data)
median_Ws = statistics.median(sample_data)
mode_Ws = stats.mode(sample_data)
geometric_mean_Ws = stats.gmean(sample_data)
harmonic_mean_Ws = statistics.harmonic_mean(sample_data)
print("Mean:", mean_Ws)
print("Median:", median_Ws)
print("Mode:", mode_Ws)
print("Geometric Mean:", geometric_mean_Ws)
print("Harmonic Mean:", harmonic_mean_Ws)