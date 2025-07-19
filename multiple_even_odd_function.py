def even_odd():
    n=int(input("enter your number  "))
    even=[]
    odd=[]
    for i in range(1,n+1):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
        return(even,odd)
    







