def remove_values_from_list(the_list, val):
        while val in the_list:
            the_list.remove(val)
            
def product_even(arr):
    #print("this"+str(arr))
    product=1
    even_list=[]
    if not arr:
        print("No Even Number Found Product Can Not Be Calculated")
    else:
        for i in arr:
            if i % 2==0:
                even_list.append(i)
                product=product*i
        print("Product Of All Even Number is " +str(product))
        print("List of Even Number"+str(even_list))    
        if not even_list:
            print("No Even Number Found Product Can Not Be Calculated n") 
    
items = []
items1 = []
n = int(input("Enter how many elements you want: "))
if n >= 1:
    for i in range(0, n):
        x = int(input("Enter the numbers into the array: "))
        items.append(x)
    remove_values_from_list(items, 0)
    #print(items)
    product_even(items) 

else:
    print("Not A valid Argument Size shoule be greater then ZERO")
