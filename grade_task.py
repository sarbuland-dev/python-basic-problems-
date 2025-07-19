def check_valid_marks(marks):
    if marks<0 or marks>100:
        print("invail entery of marks ")
        exit()
    

print("Welcome to school resulte page\n Enter your books marks below")
obtain_marks=0
grade=[]
total_marks=500


math=int(input(f"Enter your Math marks:  "))
check_valid_marks(math)
obtain_marks += math
    
english=int(input("Enter your English marks:  "))
check_valid_marks(english)
obtain_marks += english

chemistry=int(input("Enter your Chemistry marks:  "))
check_valid_marks(chemistry)
obtain_marks += chemistry

pakstudy=int(input("Enter your Pak Study marks  "))
check_valid_marks(pakstudy)
obtain_marks += pakstudy

biology=int(input("Enter your Biology marks  "))
check_valid_marks(biology)
obtain_marks += biology
    
print("Your total obtain marks are ", obtain_marks)
percentage=(obtain_marks/total_marks)*100

print("your percentage is", percentage)
if percentage>=90 and percentage<95:
    print("Congratulations! your grade is A")
elif percentage>=95 and percentage<=100:
    print("congraulations! your grade is A+")
elif percentage>=80 and percentage<85:
    print("congraulations!your grade is B")
elif percentage>=85 and percentage<90:
    print("congraulations!your grade is B+")
elif percentage>=70 and percentage<75:
    print("congraulations!your grade is C")
elif percentage>=75 and percentage<80:
    print("congraulations!your grade is C+")
elif percentage>=50 and percentage<70:
    print( "your grade is D")
elif percentage<50:
    print("Try again!! your grade is F")







