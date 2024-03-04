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
