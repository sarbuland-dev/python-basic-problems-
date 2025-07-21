def sum(x,y):
    return x+y

def subraction(x,y):
    return x-y

def multi(x,y):
    return x*y

def divion(x,y):
    return x/y



print("welcome!! menu list is here;    ")
print("1: add\n2:subraction\n3:multiplication\n4:divion")
while True:
     choice=float(input("plz select an option  "))
     if choice<=4 and choice>=1:
         break
         
     else:
         print("invalid!!! pz enter a correct option  ")

num1=float(input("Enter a number  "))
num2=float(input("Enter a number  "))

if choice==1:
    print(f"your additon of{num1} and{num2} is",sum(num1,num2))
elif choice==2:
    print(f"your subtraction of{num1} and{num2} is", subraction(num1,num2))
elif choice==3:
    print(f"your multiplication of{num1} and{num2} is", multi(num1,num2))
elif choice==4:
    print(f"your divion of{num1} and{num2} is", divion(num1,num2))


         

 




    
