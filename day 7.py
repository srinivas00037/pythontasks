#find the position of prime number
pos=7
count=0
prime=0
num=2
while count<pos:
   fators=0
   for i in range(2,num):
      if num%i==0:
         fators+=1
         break
        
   if fators==0:
      prime=num
      count+=1
   num+=1
print(f"{count} prime number is {prime} ")   

#substring exists or not 
word="radhakrishna"
substring="krish"
for i in range(len(word)):
   if substring==word[i:i+len(substring)]:
      print(f"{substring} is substring of {word} and is prasent at {i}-{i+len(substring)-1}")


#logest palindramic substring
word="malayali"
longest=""
for i in range(len(word)):
    temp=""
    for j in range(i,len(word)):
        temp+=word[j]
        if temp==temp[::-1] and len(temp)>len(longest):
            longest=temp
        
print(longest)

#count the palindramic in a sting
word="malayalam"
count=0

for i in range(len(word)):
    temp=""
    for j in range(i,len(word)):
        temp+=word[j]
        if temp==temp[::-1] and len(temp)>1:
            count+=1
print(f"total  palindramic string are {count}")

# smallest palindramic substring
word="malayalam"
smallest="malayalam"
for i in range(len(word)):
    temp=""
    for j in range(i,len(word)):
        temp+=word[j]
        if temp==temp[::-1] and len(temp)<len(smallest) and len(temp)>1:
            smallest=temp
        
if smallest!=word:
    print("smallest palindramic substring is",smallest)
else:
    print("no palindramic substring in ",word)