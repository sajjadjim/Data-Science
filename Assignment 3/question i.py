import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Define the sizes of each group
sizes = {
    '100': 20,  # Math and Statistics
    '010': 25,  # Domain Experts
    '001': 30,  # Hacking Skills
    '110': 15,  # Math and Statistics & Domain Experts
    '101': 10,  # Math and Statistics & Hacking Skills
    '011': 18,  # Domain Experts & Hacking Skills
    '111': 7    # Math and Statistics & Domain Experts & Hacking Skills
}
# Create the Venn diagram
venn = venn3(subsets=sizes, set_labels=('Math and Statistics', 'Domain Experts', 'Hacking Skills'))

# Label each subset
venn.get_label_by_id('100').set_text('Math and Statistics')
venn.get_label_by_id('010').set_text('Domain Experts')
venn.get_label_by_id('001').set_text('Hacking Skills')
venn.get_label_by_id('110').set_text('Research')
venn.get_label_by_id('101').set_text('Machine Learning')
venn.get_label_by_id('011').set_text('Danger Zone')
venn.get_label_by_id('111').set_text('Common Data Science')

# Show the plot
plt.title("Data Science Venn Diagram")
plt.show()


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