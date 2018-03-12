even_list = []
odd_list = []

def max_even_odd(max_e_o):
    max_even = 0
    max_odd = 0
    for i in max_e_o:
        if i % 2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
  
    for i in even_list:
        if i > max_even:
            max_even = i
    if max_even == 0:
        print("No Even Element In Given List")
    else:
        print("The Max Even Number in Given List is "+str(max_even))
    for i in odd_list:
        if i > max_odd:
            max_odd = i
    if max_odd == 0:
        print("No Odd Element In Given List")
    else:
        print("The Max Odd Number in Given List is "+str(max_odd))


items = []
n = int(input("Enter how many elements you want: "))
if n >= 1:
    for i in range(0, n):
        x = int(input("Enter the numbers into the array: "))
        items.append(x)
    tmp=items[0]
    tmp1=0
    equal=True
    equal1=False
    count=0
    for i in items:
        if i==0:
            count=count+1
            if count == n:
                equal1 = True
                print("All Element Are 0 Hence Is No Largest Element Even or Odd")
                break;
               
 #       else:
    for i in items:
        if tmp != i:
            equal = False
            break;
    if equal:
        print("List Contain "+str(n)+" Elements And All Are Identical")
        max_even_odd(items)

#        if items[i] == items[i+1]:
    else:
        print(items)
        max_even_odd(items)

else:
    print("Not A valid Argument Size shoule be greater then ZERO")

