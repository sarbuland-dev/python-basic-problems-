# 8. Write a program to calculate the digital root of a number (sum digits repeatedly until one digit
# remains)
n=987
while n >9:
    y=str(n)
    z=0
    
    for i in y:
        z+=int(i)
    n=z

print(n)



  

        
        
        
        
    
    
        
    
        
    
    