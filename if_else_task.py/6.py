while True:
    try:
        print("1: Celsius to Fahrenheit")
        print("2: Fahrenheit to Celsius ")
        ch=float(input(" Enter your convertion method  "))
        if ch<0 or ch>2:
            print("Enetr value in limit (1-2)")
            
        
        if ch== 1:
            while True:
                try:
                    x=float(input("Enter your Celsius temperature  "))
                    temp=((x-32)*5/9).__round__()
                    print(f"Your temperature in Fahrenheit is {temp} F")
                    if temp>86:
                        print("Its hot today!")
                    elif temp<50:
                        print("its cold today ")
                    else:
                        print("The weather is pleasant.")
                        break
                except:
                    print("Enter value in integer from ")
        
        elif ch== 2:
            while True:
                try:
                    x=float(input("Enter your Fahrenheit temperature  "))
                    temp=((x*9/5)+32).__round__()
                    print(f"Your temperature in Celsius is {temp} C")
                    if temp>30:
                        print("Its hot today!")
                    elif temp<10:
                        print("its cold today ")
                    else:
                        print("The weather is pleasant.")
                        break
                except:
                    print("Enter value in integer from ")
    except:
        print("Enter value in integer from ")
                       