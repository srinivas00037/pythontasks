#wrrite  program to print longest number in a string
senentace="hello good morning all"
words=senentace.split(" ")
long_words=""
for i in range(len(words)):
    if i<len(words[i]):
        long_words=words[i]
print(long_words,"is the largest word")


# * * * * * 
# *
# * * * * *
#         *
# * * * * *

rows=5
mid=(rows//2)+1

for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i<=mid:
            if i==1 or i==mid or j==1:
                res+="*"+" "
            else:
                res+=" "+" "
        else:
            if i==rows or j==rows:
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)

# * * * * *
#         *
# * * * * *
# *
# * * * * *

rows=5
mid=(rows//2)+1

for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i<=mid:
            if i==1 or i==mid or j==rows:
                res+="*"+" "
            else:
                res+=" "+" "
        else:
            if i==rows or j==1:
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)

# * * * * *
#         *
# * * * * *
#         *
# * * * * *
    
rows=5
mid=(rows//2)+1

for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i<=mid:
            if i==1 or i==mid or j==rows:
                res+="*"+" "
            else:
                res+=" "+" "
        else:
            if i==rows or j==rows:
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)







        
