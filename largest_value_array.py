import numpy as np    
#items=np.array([3,2,10,11,12,5])
items = []
n = int(input("Enter how many elements you want in size of array: "))
for i in range(0, n):
    x = input("Enter the numbers into the array: ")
    items.append(x)
print(items) 
n1=int(input("input nth largest values of an array to print: "))
if n1>n:
    print ("nth Element out of range")
else:
    for i in range(len(items)):
                for j in range(len(items)-1-i):
                        if items[j] > items[j+1]:
                            items[j], items[j+1] = items[j+1], items[j]    
#    print(items)
    print("The "+str(n1)+" Largest Element Is " +str(items[n1-1]) )    

