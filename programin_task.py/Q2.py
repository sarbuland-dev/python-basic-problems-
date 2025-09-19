# 2. Write a program that checks whether a given string is a palindrome ignoring spaces and
# punctuation.

try:
    x = input("Enter your text  ").strip().lower()
    y = ""
    rev = ""
    punc = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    
    for ch in x:
        if ch not in punc:
            y += ch

    
    for ch in y:
        rev = ch + rev

    
    if y == rev:
        print("This is palindrome")
    else:
        print("Not palindrome")

except:
    print("Write a string")
    
    
# second method: 
    
try:
    x = input("Enter your text  ").strip().lower()
    y = ""
    
    punc = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    
    for ch in x:
        if ch not in punc:
            y += ch
    
    lst=list(y)
    z=lst[::-1]
    srt="".join(z)
    if y==srt:
        print("This is palindrome")
    else:
        print("This is not palindrome")
except:
    print("Write a string")


    