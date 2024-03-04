import numpy as np
import matplotlib.pyplot as plt

# Create Drew Conway's Venn diagram
plt.figure(figsize=(6, 4))
plt.title("Drew Conway's Venn Diagram")
plt.text(0.5, 0.5, "Data Science", horizontalalignment='center', verticalalignment='center', fontsize=15)
plt.text(0.2, 0.6, "Hacking Skills", horizontalalignment='center', verticalalignment='center', fontsize=12)
plt.text(0.8, 0.6, "Math And Statistics", horizontalalignment='center', verticalalignment='center', fontsize=12)
plt.text(0.5, 0.3, "Domain Expert", horizontalalignment='center', verticalalignment='center', fontsize=12)
plt.axis('off')
plt.show()
