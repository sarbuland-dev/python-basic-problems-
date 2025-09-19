try:
    lst=list(map(int,input("Enter your list of integers  ").split(",")))
    n=len(lst)
    for i in range(0 ,n-1, 2):
       lst[i],lst[i+1]=lst[i+1],lst[i]
    print(lst)
        
except:
    print("invalid")   
            