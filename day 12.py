#Exception handling
#try
#except
#else
#filnally
try:
    div=10/0
except:
    print("zero divition error")
else:
    print(div)
finally:
    print("next letter")
 
#file handlig
#open():open a file or creating a file
#read():read method is reading a file 
try:
 file=open("./sample.txt","r")
 print(file.read())
except Exception as e:
 print(e)

#readline():readline is use to read single line code
try:
   file=open("./sample.txt","r")
   print(file.readline())
except Exception as e:
   print(e)
#readlines():readlines is used to read all line and pint in one line in list
try:
   file=open("./sample.txt","r")
   print(file.readlines())
except Exception as e:
   print(e)
#write():write is used to overwrite the code
try:
   file=open("./sample.txt","w")
   file.write("this is fouth line\n")
   file.write("fifth line")
except Exception as e:
   print(e)
 
#write():write is used to overwrite the code in singk line by using list
try:
   file=open("./sample2.txt","w")
   file.writelines(["this is fouth line\n","hello\n","good morning\n"])
   
except Exception as e:
   print(e)
 