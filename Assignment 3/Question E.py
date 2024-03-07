import pandas as pd
import statistics
data = pd.read_csv("../Assignment 3/Algerian_forest_Modm.csv")
# Select a random sample of size 180 with seed value 5364
sample_data = data['Ws'].sample(n=180, random_state=5364)


# e) Determine population standard deviation and population coefficient of variation
mean_Ws = statistics.mean(sample_data)
population_std_dev = statistics.pstdev(sample_data)
population_coeff_var = (population_std_dev / mean_Ws) * 100
print("\nPopulation Standard Deviation:", population_std_dev)
print("Population Coefficient of Variation:", population_coeff_var)