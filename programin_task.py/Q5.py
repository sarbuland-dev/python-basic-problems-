# 5. Write a program to count how many words in a sentence start with a vowel

try:
    srt=input("Enter your text ").strip().lower()
    vowel="aeiou"
    count=0
    for i in srt:
        for ch in vowel:
            if i==ch:
                count+=1
    print(f"your count is {count} ")
except:
    print("Plz enter a string")
    