#Claculate mean, median, mode, standard deviation, variance, Minimum, Maximum of 5, 6, 7, 10 12

import numpy as np
import pandas as pd

AA=[5,6,7,10,12]
A=pd.DataFrame(AA)

np.mean(A)
np.median(A)
np.min(A)
np.std(A)
np.var(A)
