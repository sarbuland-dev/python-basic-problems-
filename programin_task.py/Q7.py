# 7. Implement a program that reads a string and returns a dictionary of word frequencies, ignoring
# case

try:
    srt=input("enter your srting  ").strip().lower()
    al={}
    for i in srt:
        if i in al:
            al[i]+=1
        else:
            al[i]=1
    print(al)
        
except:
    print("plz enter a string")
    
    

        
    