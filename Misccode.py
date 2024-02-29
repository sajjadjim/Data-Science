#Misccode.py
wt=[21.4,19.7,19.7,20.6,20.8,20.1,19.7,20.3,20.9]
import scipy.stats as sc
res=sc.describe(wt)

import numpy as np
m=res[2]
v=res[3]
s=np.sqrt(v)

cv=(s/m)*100;cv

sc.gmean(wt)
sc.variation(wt)
#cv=(std/mean)%100


m1=100; sd1=15; 
m2=15; sd2=10;

cv1=(sd1/m1)*100
cv2=(sd2/m2)*100

cv1
cv2


sc.variation(wt)

sc.pmean(wt,1)

x1=[20,29,12,45,12,34,23]
x2=[13,5,19,39,56,78,22,34,2,5]
x3=[4,5,8,22,55,34,67,12]

cv1=sc.variation(x1);cv1

import scipy.stats as sc
def cv(xx):
    re=sc.variation(xx)
    return(re)

cv(x1)
cv(x2)




