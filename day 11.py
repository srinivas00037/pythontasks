# #comprehension
# #out=[expression loop condtion]

# #print even number

# element=[1,2,3,4,5,6,7,8,9]
# out=[n for n in element if n%2==0]
# print(out)

# #print double of numbers

# doubled=[val*2 for val in element]
# print(doubled)

# #print lower char to upper
# names=("srinivas","nani","ntr","prabhas")
# changed=[name.upper() for name in names]
# print(changed)

# #print 2 list into one list
# nested=[[1,2,3],[4,5,6]]
# single=[j for i in nested for j in i]
# print(single)

# #distnary
# num=(2,3,4,5)
# squared={x:x**2 for x in num }
# print(squared)

# #****

# string="bring me thanos"
# frq={x:string.count(x) for x in string if x!=" "}
# print(frq)
# max=0
# char=""
# for i in frq:
#     if frq[i]>max:
#         max=frq[i]
#         char=i
# print(char,max)
# #convert keys to value and value to key 
# dict={
#     "apple":"red",
#     "orange":"orannge",
#     "mango":"yellow"
# }
# changed={dict[key]:key for  key in dict }
# print(changed)

# #find count of substring
# word=("philonthophish","lollylog")
# length={key:len(key) for key in word }
# print(length)

#print the dict which  value is  greater then 50
dict={
    "a":50,
    "b":60,
    "c":70
}
greater={k:v for k,v in dict.items() if v>50 }
print(greater)

