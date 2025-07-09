# print number is prime or not 
num=int(input("enter a number:"))
factors=0
for i in range(2,num):
    if num%i==0:
        factors+=1
if factors==0:
    print(num,"is prime")
else:
    print(num,"is not prime becase it has",factors,"factors")

#print not prime of the number
num=int(input("enter a number"))
for i in range(num-1,1,-1):
    factors=0
    for j in range(2,i):
        if i%j==0:
            factors+=1
            break
    if factors==0:
        print("prives prime number is",i)
    break 

#find the next prime number
num=int(input("enter a number"))
prime_not_found=True
while prime_not_found==True:
    num+=1
    factors=0
    for i in range(2,num):
        if num%i==0:
            factors+=1
            break
    if factors==0:
        print("next prime number is",num)
        prime_not_found=False
        break

#find the nearest prime number
num=59
prime_not_found=True
while prime_not_found==True:
    num+=1
    factors=0
    next_prime=0
    for i in range(2,num):
        if num%i==0:
            factors+=1

            break
    if factors==0:
      
        prime_not_found=False
        next_prime=num
        break
num=59
for i in range(num-1,1,-1):
    factors=0
    pre_prime=0
    for j in range(2,i):
        if i%j==0:
            factors+=1
            pre_prime=i
            break
   
        
    break 
print(pre_prime,num,next_prime)
if (num-pre_prime)<(num-next_prime):
    print(next_prime,"is nearest")
elif (num-pre_prime)>(num-next_prime):
    print(next_prime,"is nearst")
else:
    print("both are equal distance")

#two string are anagram or not
s1=input("enter a name:")
s2=input("enter another name:")
if len(s1)!=len(s2):
    print(s1,s2,"not anagram")
else:
    is_anagram=True
for i in s1:
    print(s1.count(i),s2.count(i))
    if s1.count(i)!=s2.count(i):
        print(s1,s2,"is not anagram")
        is_anagram=False
        break
if is_anagram==True:
    print(s1,s2,"is anagram")
else:
    print(s1,s2,"is not anagram")


