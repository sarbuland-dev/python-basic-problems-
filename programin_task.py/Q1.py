# 1. Write a program that takes a list of integers and removes all duplicates without using set()

lst=[1,2,3,3,3,4]
x=[]
for i in lst:
    if i not in x:
        x.append(i)
    else:
        x.remove(i)
print(x)
    