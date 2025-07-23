
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
print("choose claculation to preform: \n",
"1.Add\n",
"2.subtract\n",
"3.multipication\n",
"4.Divide\n")
cal=input().strip().lower()
if cal=="add" or cal== "1":
    ans=num1+num2
elif cal=="subtract" or cal=="2":
    ans=num1-num2
elif cal=="multipucation"or cal=="3":
    ans=num1*num2
elif cal=="Divide" or  cal=="4":
    if num2==0:
        print("Error! can't divide by zero")
    else:
        ans=num1/num2
else:
    print("Invalid opreation!")
    ans=None
if ans is not None:
    print(f"the Answer is: {ans}")

