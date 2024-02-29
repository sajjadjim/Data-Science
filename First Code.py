#DIU_315_1.py.docx
import numpy as np
import pandas as pd
import scipy.linalg as slin 

dob=pd.read_csv("C:/Users/HP/Desktop/315/obli.csv")
dnonc=pd.read_csv("C:/Users/HP/Desktop/315/nonc.csv")

Z2=np.transpose(dob[["activity","antigen"]])
Z1=np.transpose(dnonc[["activity","antigen"]])

S1=np.cov(Z1,bias=False);S1
S2=np.cov(Z2,bias=False);S2

X1b=np.mean(Z1,axis=1);X1b
X2b=np.mean(Z2,axis=1);X2b

n2=len(dob); n1=len(dnonc)

Sp=((n1-1)/((n1-1)+(n2-1)))*S1+((n2-1)/((n2-1)+(n2-1)))*S2;Sp
#Spp=(29/73)*S1+(44/73)*S2;Spp

SpI=np.linalg.inv(Sp); 

X12=X1b-X2b;X12
yh=np.dot(X12,SpI);yh

U=X1b+X2b
mhat=np.dot((1/2)*yh,U)

x0=[-.0867,-0.07786]

#x0=[-.1744,.1892]

#v1 = float(input("Please provide 1st value: "));v2 = float(input("Please provide 2nd value: "));#x0=[v1,v2]

rule=np.dot(yh,x0)-mhat;rule

if rule>0:
    print("Subject/individual belongs to Goup 1")
else:
    print("Subject/individual belongs to Goup 2")

#--------------------------------------#


##
np.array([[ 64.96,  33.2 , -24.44],
       [ 33.2 ,  56.4 , -24.1 ],
       [-24.44, -24.1 ,  75.56]])


import numpy as np

A = [45, 37, 42, 35, 39]
B = [38, 31, 26, 28, 33]
C = [10, 15, 17, 21, 12]



##
