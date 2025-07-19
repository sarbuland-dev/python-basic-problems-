def sum():
    n=int(input("enter your number  "))
    num=0
    for i in range(1,n+1):
        num+=i
    return(f"number  {n}  is  {num}")
        


y=sum()
print(y)