import numpy as np
x=np.array([4,2,6,1,1,5])
y=np.array([3,2,10,11,12,5,4,20])

#i row -> x
#j cplumn -> y
#matrix should be 6*8
yj=0
xi=0
#c[0][0]
c = np.zeros((6,8))

for row_index, row in enumerate(x):
    for col_index, item in enumerate(y):
        #print("row_i "+str(row_index)+" col_i "+str(col_index))
        #print(x[row_index],y[col_index])
        xi=x[row_index]
        #print(y[col_index])
        yj=y[col_index]
        c[row_index][col_index]=(1/xi-yj)

print(c)        
