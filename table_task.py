# def table(n):
    
#     for i in range(1,11):
#         print(n,"X",i,"=",n*i,)

# n=int(input("enter your number "))
# table(n)

# ++++++++++++++=++++++++++++++++++=
def table(n,r):
    
    for i in range(1,r+1):
        print(n,"X",i,"=",n*i)

n=int(input("Plz enter table number "))
r=int(input("Plz enter table range "))
table(n,r)