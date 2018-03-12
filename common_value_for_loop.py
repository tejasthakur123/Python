import numpy as np
x=np.array([4,2,6,1,1,5])
y=np.array([3,2,10,11,12,5])
z=[]
for i in x:
    for j in y:
        if( i==j):
            z.append(i)#Creating another list 

print("The Common Values In Given Array Are: "+str(z))
