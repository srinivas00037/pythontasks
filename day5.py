#given number is armstrong number or not
num=8208
num2=8208
num3=8208
count=0
while num!=0:
    num=num//10
    count+=1
print(count)
m=0
while num2!=0:  #153!=0 15!=0 1!=0
    last_digit=num2%10 #3 5 1 0 
    m=(last_digit**count)+m #
    num2=num2//10  
if m==num3:
    print("armstrong")
else:
    print("not armstring")


#febnosis series
a=0
b=1
for i in range(14):
    print(a)
 
    c=a+b
    a=b
    b=c

    
