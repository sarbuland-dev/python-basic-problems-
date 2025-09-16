import math


a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))


D = b**2 - 4*a*c

print(f"Discriminant = {D}")


if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Do real aur alag roots hain:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif D == 0:
    root = -b / (2*a)
    print("Do real aur barabar roots hain:")
    print("Root =", root)

else:
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)   
    print("Complex roots hain:")
    print("Root 1 =", real, "+", imag, "i")
    print("Root 2 =", real, "-", imag, "i")
