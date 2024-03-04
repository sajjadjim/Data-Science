import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Given data points for FWI and RH
RH = np.array([79, 67, 63, 56])
FWI = np.array([0.21, 2.5, 10.2, 6.1])

# Estimate Fisher Linear Discriminant Function
X = np.column_stack((RH, FWI))
y = np.array([1, 1, 2, 2])  # Assuming 1 for "fire" and 2 for "not fire"

lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

# Classify the given points
new_data = np.array([[79, 0.21], [67, 2.5], [63, 10.2], [56, 6.1]])
predicted_classes = lda.predict(new_data)

for i in range(len(new_data)):
    print(f"FWI: {new_data[i][1]}, RH: {new_data[i][0]}, Classified as: {'fire' if predicted_classes[i] == 1 else 'not fire'}")