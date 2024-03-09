import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy import stats

# Import the CSV file
data = pd.read_csv("weather_data.csv")

# Extract FFMC values
ffmc_values = data['FFMC']

# b) Construct a histogram
plt.figure(figsize=(10, 6))
plt.hist(ffmc_values, bins=20, edgecolor='black')
plt.title('Histogram of FFMC Values')
plt.xlabel('FFMC')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# c) Calculate mean, median, mode, geometric mean, and harmonic mean
mean_ffmc = np.mean(ffmc_values)
median_ffmc = np.median(ffmc_values)
mode_ffmc = statistics.mode(ffmc_values)
geometric_mean_ffmc = stats.gmean(ffmc_values)
harmonic_mean_ffmc = statistics.harmonic_mean(ffmc_values)

print("Mean:", mean_ffmc)
print("Median:", median_ffmc)
print("Mode:", mode_ffmc)
print("Geometric Mean:", geometric_mean_ffmc)
print("Harmonic Mean:", harmonic_mean_ffmc)

# d) Report five summary measures and construct a box plot
q1_ffmc = np.percentile(ffmc_values, 25)
q3_ffmc = np.percentile(ffmc_values, 75)
iqr_ffmc = q3_ffmc - q1_ffmc
minimum_ffmc = min(ffmc_values)
maximum_ffmc = max(ffmc_values)

plt.figure(figsize=(8, 6))
plt.boxplot(ffmc_values, vert=False)
plt.title('Box Plot of FFMC Values')
plt.xlabel('FFMC')
plt.grid(True)
plt.show()

print("Minimum:", minimum_ffmc)
print("1st Quartile:", q1_ffmc)
print("Median:", median_ffmc)
print("3rd Quartile:", q3_ffmc)
print("Maximum:", maximum_ffmc)

# e) Determine population standard deviation and population coefficient of variation
population_std_dev_ffmc = statistics.pstdev(ffmc_values)
population_coeff_var_ffmc = (population_std_dev_ffmc / mean_ffmc) * 100

print("Population Standard Deviation:", population_std_dev_ffmc)
print("Population Coefficient of Variation:", population_coeff_var_ffmc)

# f) Determine the coefficient of skewness and kurtosis
skewness_ffmc = statistics.skew(ffmc_values)
kurtosis_ffmc = statistics.kurtosis(ffmc_values)

print("Coefficient of Skewness:", skewness_ffmc)
print("Kurtosis:", kurtosis_ffmc)

# g) Covariance and correlation matrices
covariance_matrix = data[['Temp', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI']].cov()
correlation_matrix = data[['Temp', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI']].corr()

print("Covariance Matrix:")
print(covariance_matrix)
print("\nCorrelation Matrix:")
print(correlation_matrix)

# h) Regression equation of FWI on RH
fwi_values = data['FWI']
rh_values = data['RH']

slope, intercept, r_value, p_value, std_err = stats.linregress(rh_values, fwi_values)

print("Regression Equation: FWI = {:.2f} * RH + {:.2f}".format(slope, intercept))
# Estimate FWI when RH is 21.5%
rh = 21.5
estimated_fwi = slope * rh + intercept
print("Estimated FWI when RH is 21.5%:", estimated_fwi)
