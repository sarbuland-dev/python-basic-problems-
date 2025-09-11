def weekday(n):
    
    match n:
     case 1:
        return(" Today is Monday !")
     case 2:
        return(" Today is Tuesday !")
     case 3:
        return(" Today is Wednesday! ")
     case 4:
        return(" Today is Thursday! ")
     case 5:
        return("Today is Friday! ")
     case 6:
        return("Today is Saturday! ")
     case 7:
        return("Today is Sunday! ")
     case _:
        return("Please! Enter a valid day number ")
       

print(weekday(1))
print(weekday(5))
print(weekday(7))
print(weekday(10))
        
    
