# # #non mutal values
# # #count
# # animals=["cat","dog","lion","tiger","cat","gorilla"]
# # times=animals.count("cat")
# # print(times)

# # #index
# # animals=["cat","dog","lion","tiger","cat","gorilla"]
# # print(animals.index("cat"))

# # #copy
# # color=["green","red","pink","blue","orannge"]
# # print(color.copy())

# # # count number of apple in a list without using method
# # fruits=["apple","banana","guava","orange","papaya","banana","apple"]
# # val="apple"
# # count=0
# # for i in range (len(fruits)):
# #     if  fruits[i]==val:
# #         count+=1
# # print(f"{val} is present in {count} times")

# # #find the index
# # fruits=["apple","banana","guava","orange","papaya","banana","apple"]
# # val="apple"
# # for i in range (len(fruits)):
# #     if  fruits[i]==val:
# #         print(i)
# #         break

# # #sum
# # num=[1,2,3,4,5,-6]
# # print(sum(num))

# # #min
# # small=min(0,-2)
# # print(small)

# # find the third highest using funtion
# # num=[1,44,56,76,7,87,85,93,45,65]
# # pos=2
# # def find_highest(li,n):
# #     if len(li)>n:
# #         return not posible
# #     else:
# #         for i in range(n):
# #             li.remove(max(li))
# #             return li
# # print(find_highest(num,pos)) 




# #to remove duplicates and find third highest 
# num=[7,4,5,66,56,66,65,56]
# unq_num=[]
# for i in num:
#     if i not  in unq_num:
#         unq_num.append(i)
# print(unq_num)
# pos=4
# if len(unq_num)<pos:
#     print("not posible")
# else:
#     for i in  range(pos-1):
#         unq_num.remove(max(unq_num))
#     print(max(unq_num))


# #find max value with out using method
# num=[253,254,56,45,6,4,73,67,75]
# temp=num[0]
# for i in num:
#     if i>temp:
#         temp=i
# print(temp)

# #find min value with out using method
# num=[253,254,56,45,6,4,73,67,75]
# temp=num[0]
# for i in num:
#     if i<temp:
#         temp=i
# print(temp)
# #find sum of valuesin a list with out using method
# num=[1,2,3,4,5,6]
# temp=0
# for i in range(len(num)):
#     temp+=i
# print(num)


# #find index with out using method
# food=["biriyani","fired_rice","momo","pizza","manchuriya","mono"]
# val="mono"
# for i in range(len(food)):
#     if food[i]==val:
#         print(f"{val} is present at {i} index")

# #find count  with out using method
# food=["biriyani","fired_rice","momo","pizza","manchuriya","momo"]
# val="momo"
# count=0
# for i in range(len(food)):
#     if food[i]==val:
#         count+=1
# print(f"{val} is presnt {count} times")


char=["A","B","2","u","z","4"]
upper=[]
lower=[]
sum=0
for i in char:
    if 97<=ord(i)<=122:
        lower.append(i)
    elif 65<=ord(i)<=90:
        upper.append(i)
    else:
        sum+=int(i)
print(f"upper:{"".join(upper)} lowerlist:{"".join(lower)} and sum of numbers{sum}")
        


