while True:
  try:
      year=int(input("Enter your year  "))
      month=int(input("Enter your month "))
      if year<=0 :
           print("Enter a postive number ")
      if year>=0:
          month=int(input("Enter your month "))
          if month<=0:
              print("Enter postine number  ")
              if month==1:
                  print("jan have 30 days")
            
          
              
      else:
          break
      
  except:
      print("Enter year/month in integer from plz. ")

