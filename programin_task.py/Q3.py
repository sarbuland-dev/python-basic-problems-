# 3. Write a program to find the second largest element in a list without sorting.

lst=[2,3,1,56,4,90,96,100,89,103]
large=None
second=None
for i in range(len(lst)-1):
    if lst[i]>lst[i+1]:
        large=lst[i]
        second=lst[i+1]
    elif lst[i]<lst[i+1]:
        large=lst[i+1]
        second=lst[i]
    elif lst[i]>second and lst[i]!=large:
        second=lst[i]
        
# print(large)
print(second)