# Create a function to rotate a list k steps to the right (without using slicing).
def rotate_right(lst, k):
    n = len(lst)
    k = k % n   
    
    for _ in range(k):
        last = lst.pop()     
        lst.insert(0, last)  
    return lst



print(rotate_right([1, 2, 3, 4, 5,9],1))  



# y=[[1,2,[3,4,5],[6,7,8]]]
# lst=[]
# for i in y:
#     for j in i:
#         lst.append(j)

# print(lst)

# n="ali-ahmad"
# x=n.split("-")
# print(x)
    






