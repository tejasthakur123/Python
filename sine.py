#Solution 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)        

def sin(x,n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        sine = sine + ((y**(2.0*i+1))/factorial(2*i+1))*sign
    return sine

x=int(input("Enter the value of x in degrees:"))
#n=int(input("Enter the number of terms:")) # can be ask to user and replace the value of 25 with n in below line
print("The Value of Sin "+str(x)+" is :"+str(round(sin(x,25),2)))



#solution 2
def power(x, y):
    if y == 0:
        return 1
    if y >= 1:
        return x * power(x, y - 1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)        

x1 = float(input("Enter Value Of Sin X: "))
n=3
m=5
tmp1=0
pi=22/7
x=x1*(pi/180) #Calculate redian

#Calculate negative part
for i in range(26):
    #print(i)
    tmp=(power(x,n)/factorial(n))
    n=n+4
    tmp1=tmp+tmp1
    
tmp=0
tmp2=0
#Calculate positive part
for i in range(26):
    #print(i)
    tmp=(power(x,m)/factorial(m))
    n=n+4
    tmp2=tmp+tmp2

print(x-(-tmp1+tmp2))

