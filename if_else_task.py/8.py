amount = 50000
while True:
    try:
        print("\n--- ATM MENU ---")
        print("1: Check balance")
        print("2: Withdraw money")
        print("3: Deposit money")
        print("4: Exit")
        
        bal = int(input("Enter your option: "))
        
        if bal == 1:  
            print(f"Your balance is {amount}")  
        
        elif bal == 2:  
            while True:
                try:
                    x = float(input("Enter your amount to withdraw: "))
                    if x <= 0:
                        print("Enter a valid positive amount ")
                    elif x > amount:
                        print("Insufficient balance ")
                    else:
                        amount -= x
                        print(f"Your amount {x} is withdrawn and now your total balance is {amount}")
                        break
                except:
                    print("Enter your amount in number ")
                    
        elif bal == 3:  
            while True:
                try:
                    x = float(input("Enter your amount to deposit: "))
                    if x <= 0:
                        print("Enter a valid positive amount ")
                    else:
                        amount += x
                        print(f"Your amount {x} is deposited and now your total balance is {amount}")
                        break
                except:
                    print("Enter your amount in number ") 
        
        elif bal == 4:  
            print("Thank you for using ATM. Goodbye!")
            break
        
        else:
            print("Enter valid option please ")
            
    except:
        print("Enter your option in number ")
              
                    
        
        
        