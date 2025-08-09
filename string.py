# # sentence="srinivas is a good boy"
# # for i in range(len(sentence)):
# #     c=sentence[i]
# #     if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
# #         print(c,"is in",i,"index")


# # sentence="srinivas is a good boy" #ovels
# # for index in range(len(sentence)):
# #     c=sentence[index]
# #     if (c=="a" or c=="e" or c=="i" or c=="o" or c=="u") and (index%2==0):
# #         print(c,index)


# # sentence="srinivas is a good boy"
# # for index in range(len(sentence)):
# #     c=sentence[index]
# #     if (c!="a" and c!="e" and c!="i" and c!="o" and c!="u" and c!=" ") and (index%2==0):
# #         print(c,index)

# # word="srinivas is good boy"
# # word=word.upper()
# # print(word)


# # word="SRINIVAS IS GOOD BOY"
# # word=word.lower()
# # print(word)

# #strip
# # user_name=input("enter a name")
# # user_nmae=user_name.strip()
# # print(user_name,len(user_name))
# # print(user_name=="mani kanta")
# #lstrip
# # user_name="     python  "
# # user_name=user_name.lstrip()
# # print(user_name,len(user_name))
# #rstrip

# # user_name="     python  "
# # user_name=user_name.rstrip()
# # print(user_name,len(user_name))
# #count
# # sentance="i am learning PYTHON "
# # upper_count=0
# # for i in range(len(sentance)):
# #     if sentance[i]==sentance[i].upper() and sentance[i]!=" ":
# #         upper_count+=1
# # print(upper_count)

# # sentence="srinivas"
# # count=0
# # for index in range(len(sentence)):
# #     c=sentence[index]
# #     if (c!="a" and c!="e" and c!="i" and c!="o" and c!="u"):
# #         count+=1
# # print("count of owels",count)
# #count the upper and lower letters in string
# # def lower_upper_count(string):
# #     upper_count=0
# #     lower_count=0
# #     for i in range (len(string)):
# #         c=string[i]
# #         if c==c.upper() and c!=0:
# #             upper_count+=1
# #         elif c==c.lower() and c!=0:
# #             lower_count+=1
# #     print("count of lower is",lower_count)
# #     print("count of upper is",upper_count)
# # lower_upper_count("sriidn DWFEWBU dehsb")

# # def char_in_index(string,num):
# #     for i in range(len(string)):
# #         char=string[i]
# #         if i%num==0 and char!="":
# #             print(char,i)
# # char_in_index("busacbcu xuasuycbku ddx",4) 
        

# #slice  slice[start:stop:count]
# word="arundhathi" #print first 4 letters amd last 4 letters and 2 multiples
# print(word[0:4:1])
# print(word[len(word)-4:len(word)])
# print(2)

# #print is palindrome or not
# word="markram"
# if word==word[::-1]:
#     print("palindrame")
# else:
#     print("not palindrame")

# # sub str ois part of string or not 
# word=input("enter a word:")
# sub_string=input("enter a sub string")
# sub_len=len(sub_string)
# for i in range(len(word)):
#     if(word[i:i+sub_len]==sub_string):
#         print(sub_string,"is part of",word)
#         break


# word=input("enter a word:")
# sub_string=input("enter a sub string:")
# sub_len=len(sub_string)
# for i in range(len(word)):
#     part=word[i:i+sub_len]
#     print(part)
#     if part==sub_string:
#         print(sub_string,"is part of",word)
#         break


# sentence="hi hello good morning mom"
# sentence=sentence.split(" ")
# palindrame_exists=False
# for i in range(len(sentence)):
#     if sentence[i][::-1]==sentence[i]:
#         palindrame_exists=True
#         print("it is palindrame")
#         break
# if palindrame_exists==False:
#     print("not palindrame")


# sentence="hi hello mom good mom morning mom"
# sentence=sentence.split(" ")
# palindrame_exists=False
# count=0
# for i in range(len(sentence)):
#     if sentence[i][::-1]==sentence[i]:
#         palindrame_exists=True
#         count+=1
# print("count of palindrame is:",count)
# if palindrame_exists==False:
#     print("not palindrame")
