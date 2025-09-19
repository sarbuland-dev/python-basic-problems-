# 4. Given a number n, print a triangle pattern of * with n rows (like a right-angled triangle).

n=15
for i in range(n+1):
    for j in range(i+1):
        print("*",end="")
    print()

