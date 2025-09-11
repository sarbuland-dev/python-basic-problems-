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

while True:        
  day=int(input("Enter your number to find day (1 to 7)  ").strip())
  print(weekday(day))
        
    
