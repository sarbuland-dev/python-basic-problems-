def greeting(details):
    
    l=len(details)
    match details:
        case _ if details[0] == ("Morning" or "Evening"or "Night"):
                match l:
                 case _ if l<=2:
                   return(f"good {details[0]} {details[1]}")
                 case _ if l>2:
                   for i in range(1,len(details)):
                    print (f"good {details[0]} {details[i]}")
        case _:
            return("somthing went wrong!")

            
               
            
    
lst=list((input("enter your time and name (plz first enter time then name  )  "  ).capitalize().strip()))
print(greeting(lst))