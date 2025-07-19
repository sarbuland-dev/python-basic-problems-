n=int(input("welcome to school grade page\n enter your numbers  "))
y=float(input("enter total number     "))
percentage=(n/y)*100
if percentage>=0 and percentage<41:
    print("F")
elif percentage>=41 and percentage<=65:
    print("D")
elif percentage>65 and percentage<=75:
    print("C")
elif percentage>=76 and percentage<=85:
    print("B")
elif percentage>=86 and percentage<=100:
    print("A")
else:
    print("invalid")