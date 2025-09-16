while True:
    try:
        x=float(input("enter your payable amount  "))
        if x<0:
            print("Enter a valid amount ")
        
        if x>50000:
            y=x*(20/100)
            total=x-y
            print(f"you get 20% discount and now your payable amount is {total}")
        elif 20000<=x<=49999:
            y=x*(15/100)
            total=x-y
            print(f"you get 20% discount and now your payable amount is {total}")
        elif 10000<=x<=19999:
            y=x*(10/100)
            total=x-y
            print(f"you get 20% discount and now your payable amount is {total}")
        elif 5000<=x<=9999:
            y=x*(5/100)
            total=x-y
            print(f"you get 20% discount and now your payable amount is {total}")
        elif x<5000:
            print("there is no discount for you ")
            
    except:
        print("Plz enter in integer from ")