import pandas as pd
import scipy.stats as stats
# Read the CSV data
data = pd.read_csv("../Assignment 3/Algerian_forest_Modm.csv")
# Select a random sample of size 180 with seed value 5364
sample_data = data['Ws'].sample(n=180, random_state=5364)

# h) Estimate the regression equation of Temperature on RH
# Assuming RH as independent variable (X) and Temperature as dependentvariable (Y)
RH = data['RH'].sample(n=180, random_state=5364)
Temperature = data['Temperature'].sample(n=180, random_state=5364)
RH_reshaped = RH.values.reshape(-1, 1)
# Fit the linear regression model
reg_model = stats.linregress(Temperature,RH)
# Extract the regression coefficients
slope = reg_model.slope
intercept = reg_model.intercept
print("\nRegression Equation:")
print(f"RH = {slope:.4f} * Temperature + {intercept:.4f}")
# Estimate RH when Temperature is 21.5%
predicted_rh = slope * 21.5 + intercept
print("Estimated RH when Temperature is 21.5%:", predicted_rh)