# 6. Write a function that takes a list of names and prints them in alphabetical order without using
# sorted().


    
    
names = ["Ali", "Sara", "ahmed", "John", "Zara"]

n = len(names)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if names[j].lower() < names[min_index].lower():  # compare alphabetically
            min_index = j
    # swap
    names[i], names[min_index] = names[min_index], names[i]

print("Ordered names:", names)
