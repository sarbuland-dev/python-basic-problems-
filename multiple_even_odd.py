n=int(input("enter your range  "))
even=[]
odd=[]


for i in range(1,n+1):
    if i%2==0:
      even.append(i)  

        
      
    else:
        odd.append(i)
        
        

print("your even numbers is ",even)
print("your odd number is ",odd)