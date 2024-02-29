#StatisticsCT_24Feb.py
# Data Set used in correlation and regression
x=[9,7,11,12,8,7,8,11,10,12,6,6]
y=[8.1,6,3.6,4,5,10,7.6,8,8,6,8.6,8]

#Descriptive statistics USING pandas
import pandas as pd
xd=pd.DataFrame(x)
xd.describe()
xd.mean()
xd.median()
xd.mode()
xd.var()
xd.skew()
xd.kurt()

#descriptive statistics USING statistics
import statistics
statistics.harmonic_mean(x)
statistics.geometric_mean(x)
statistics.mean(x)
statistics.median(x)
statistics.mode(x)
statistics.pstdev(x)
statistics.stdev(x)
statistics.pvariance(x)
statistics.variance(x)

# COVARIANCE, CORRELATION, AND REGRESSION
#DATA
x=[9,7,11,12,8,7,8,11,10,12,6,6]
y=[8.1,6,3.6,4,5,10,7.6,8,8,6,8.6,8]

import numpy as np
r = np.corrcoef(x, y) #creating correlation matrix
np.cov(x,y) # Calculates variance-Covariance Matrix
r
r[0,1]
r[1,0]

#USING pandas
import pandas as pd
xd=pd.DataFrame(x)
yd=pd.DataFrame(y)
xd=pd.Series(x)
yd=pd.Series(y)

xd.corr(yd) # Calculates correlation coefficient between x and y
yd.corr(xd) # Calculates correlation coefficient between x and y

yd.cov(xd) # Calculates Covariance between x and y


#SCATTER PLOT 
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.show()

# Add title and axis labels
plt.title("Figure: Scatter plot between car's ages and selling prices")
plt.xlabel("Age of Car in years (X)")
plt.ylabel("Selling Price of Car (Y)")
plt.scatter(x, y)
plt.show()


#Histogram
plt.hist(x)
plt.show() 


# b, a, r, pvalue, standard_error
x=[9,7,11,12,8,7,8,11,10,12,6,6]
y=[8.1,6,3.6,4,5,10,7.6,8,8,6,8.6,8]
from scipy import stats
slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)
slope
intercept
stats.linregress(x, y) # Returns b, a, r, pvalue, standard_error
