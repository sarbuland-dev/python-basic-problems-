# Write a program that accepts a sentence and outputs the word with the maximum number of
# 

def max_consonant_word(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split()   
    max_word = ""
    max_count = 0

    for word in words:
        count = 0
        for ch in word:
            if ch.isalpha() and ch not in vowels:  
                count += 1
        if count > max_count:
            max_count = count
            max_word = word

    return max_word, max_count



sentence = input("Enter a sentence: ")
word, count = max_consonant_word(sentence)
print(f"Word with maximum consonants: {word} (consonants = {count})")
