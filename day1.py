# Check whether the char is lower,upper,number using function

def check_char(char):
    code=ord(char)
    if 97<=code<=122:
        print("lower")
    elif 65<=code<=90:
        print("upper")
    elif 48<=code<57:
        print("number")
    else:
        print("another charater")
check_char("D")

 #(hello-hfllp)write function to convert vowel char into next char
def vowel_char(sentance):
    word=""
    for i in range(len(sentance)):
        if sentance[i]=="a" or sentance[i]=="e" or sentance[i]=="i" or sentance[i]=="o" or sentance[i]=="u":
            code=ord(sentance[i])
            new_code=chr(code+1)
            word+=new_code
        else:
            word+=sentance[i]
    print(word)
vowel_char("hello")
        
            



