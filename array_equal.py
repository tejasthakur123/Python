array1 = np.random.rand(10)
array2 = np.random.rand(10)
#array1 = np.array([4,2,6,1,1,5])
#array2 = np.array([4,2,6,1,1,2])
c=[]
print(array1)
print(array2)
     
for row_index, row in enumerate(array1):
    for col_index, item in enumerate(array2):
        if row_index==col_index and row==item:
            c.append(row_index)
#            print("The Random Array Are Equal At Position " +str(row_index)+" and value is "+str(item) )
#print(len(c))
#print(len(array1))
if len(c)==len(array1):
    print("The Random Array Are Equal")
else:
    print("The Random Array Are NOT Equal")
