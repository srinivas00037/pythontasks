# file=open("sample3.txt","a") 
# file.write("hello good morning")


# file=open("sample.txt","w")
# file.write("")


#fluch()
# file=open("sample.txt","w")
# file.write("this is the new line")
# file.flush()
# file.write("\nthis is  third line")
# file.close()

#seek()=it move the cousor specified or given position
file=open("sample3.txt")
file.seek(10) 
print(file.read())
#tell()= it tell user position
file=open("sample3.txt")
file.seek(4)
print(file.tell())

#oop object orented programming
class bullduzer:
    tyre="belt"
b1=bullduzer
print(b1.tyre)