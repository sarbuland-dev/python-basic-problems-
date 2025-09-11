def intr(details):
    amount= ( details[0])
    time= (details[1])
    
    match amount:
        case _ if amount <10000:
            rate=(amount*10*time)/100
            return (f"your interest is :::::  {rate} ::::   ")
        case _ if amount >= 10000:
            rate=(amount*15*time)/100
            return(f"your interest is :::::  {rate} ::::   ")
        

print(intr([5000,5]))
print(intr([15000,3]))





        
        
        
