def position(n,y):
    if n==y:
        return("equal")
    elif n>y:
        return(n," greater")
    elif n<y:
        return(n,"smaller")

n=int(input("enter your number "))
y=int(input("enter your number "))
print(position(n,y))