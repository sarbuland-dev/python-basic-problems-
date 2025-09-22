# 1. Write a program that takes a list of integers and removes all duplicates without using set()

lst=[1,2,3,3,3,4]
x=[]
for i in lst:
    if i not in x:
        x.append(i)
    else:
        x.remove(i)
print(x)

# R Work
n=[1,2,2,3,4,4]
y=0
for i in n:
    if n.count(i)==1:
        y+=i

print(y)
    

    