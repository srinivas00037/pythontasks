#find the lcm of 2 numbers using with out using bulit funtion
n1=31
n2=21
big,small=(n1,n2) if n1>n2 else n2>n1
if big%small==0:
    print(big,"is a lcm")
else:
    lcm_not_found=True
    temp_lcm=big+big
    while lcm_not_found==True:
        if temp_lcm%n1==0 and temp_lcm%n2==0:
            print(temp_lcm,"is a lcm")
            break
        else:
            temp_lcm+=big


#find the Greatest Common Divisor 
n1=30
n2=15
small=0
if n1<n2:
    small=n1
else:
    small=n2
gcd=0
for i in range(1,small+1):
    if n1%i==0 and i%n2==0:
        gcd=i
print(gcd)

#convert min in hours
min=181
hrs=min//60 
rem=min%60
if rem==0:
    print("time is",hrs,"hrs")
else:
    print("time is",hrs,"hrs",rem,"mins")

#number is perfect or not
n=28
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print("perfect number")
else:
    print("not perfect")

    


