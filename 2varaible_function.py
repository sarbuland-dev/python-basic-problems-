def sum():
    y=int(input("enter number "))
    x=int(input("enter number "))
    if (x and y)>100:
        return("no we can add")
    else:
        return(f"your numbers {x+y}")

print(sum())