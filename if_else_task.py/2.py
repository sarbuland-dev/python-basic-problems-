year=int(input("Enter your saal   "))
month= int(input("Enter your  mahina  (1-12)  "))
if month>=1 and month<=12:
    
    if month==1:
        print("January has 31 days ")
    elif month==2:
        if year%4==0:
            if year%100!=0:
                print("February has 29 days ")
            elif year%100==0:
                if year%400==0:
                    print("February has 29 days ")
                else:
                    print("February has 28 days")
        else:
            print("February has 28 days")
          
    elif month==3:
        print("March has 31 days ")
    elif month==4:
        print("April has 30 days ")
    elif month==5:
        print("May has 31 days ") 
    elif month==6:
        print("June has 30 days ")
    elif month==7:
        print("July has 31 days ")
    elif month==8:
        print("August has 31 days ")
    elif month==9:
        print("September has 30 days ")
    elif month==10:
        print("October has 31 days ")
    elif month==11:
        print("November has 30 days ")
    elif month==12:
        print("December has 31 days ")
else: 
    print("Invaid month")          
        
        
#    (year%4==0 and year%100!=0) or (year%400==0) 