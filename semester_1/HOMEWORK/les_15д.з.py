n=int(input("Введите число:"))
f= 1
while n > 1:
    f =n*f  #(f*=n)
    n -= 1
print(f)


import math
n = int(input("Введите число:"))
print(math.factorial(n))

# ==============================================================

s="codewars"
n=len(s)  
for i in range(n): 
    result=s[i]+s[n-1]
    if i>=n or i==n:
        break
    n-=1
    print(result, end="")
print('\n', s)


s="white"
n=len(s)
i=0
while i<=n:
    result=s[i]+s[n-1]
    i=i+1
    n-=1
    print(result, end="")
print('\n', s)

    