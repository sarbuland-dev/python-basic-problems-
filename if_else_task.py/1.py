n=int(input("Enter your marks (0-100)  "))
if n>=0 and n<=100:
    if n>=90 and n<=100:
        print("A+")
    elif n>=80 and n<=89:
        print("A")
    elif n>=70 and n<=79:
        print ("B")
    elif n>=60 and n<=69:
        print("C")
    elif n>=50 and n<=59:
        print("D")
    elif n>=40 and n<=49:
        print("E")
    elif n>=0 and n<=39:
        print("F")
else:
    print("Invalid Marks!")

x = [1, 2, 3]
y = x
y.append(4)

print("x =", x)
print("y =", y)
print(x is y)



