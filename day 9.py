#     a 
#    b c 
#   d e f
#  g h i j
# k l m n o

rows=5
code=97
for i in range(1,rows+1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+=chr(code)+" "
        code+=1
    print(res)

# *     *
#  *   *
#    *
#    *
   *
rows=5
mid=(rows//2)+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if mid>=i:
            if(i==j or i+j==rows+1):
                res+="*"+" "
            else:
                res+=" "+" "
            
        else:
            if(j==mid):
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)


# *        *
# * *    * *
# *   *    *
# *        *
# *        *
rows=5
mid=(rows//2)+1
for i in range(1,rows+1):
    res=" "
    for j in range(1,rows+1):
        if mid>=i:
            if i==j or i+j==rows+1 or j==1 or j==rows:
                res+="*"+" "
            else:
                res+=" "+" "
        else:
            if j==1 or j==5:
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)


# *     *
#  *   *
#    *
#   *
#  *
rows=5
mid=(rows//2)+1
for i in range(1,rows+1):
    res=" "
    for j in range(1,rows+1):
        if mid>=i:
            if i==j or i+j==rows+1 :
                res+="*"+" "
            else:
                res+=" "+" "
        else:
            if i+j==rows+1 :
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)



word="aaabcdefgabcdef"
longest=""
for i in ra"nge(2, len(word)):
    temp=""
    for j in range(i,len(word)):
        if word[j] in temp:
            break
        else:
            temp+=word[j]
    if len(temp)>len(longest):
        longest=temp
print(longest)
       



