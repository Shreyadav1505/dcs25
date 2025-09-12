a=0
b=1
# n=5
# n=0
# n=10
n=1000
for i in range(n-1):
    c=a+b
    a=b
    b=c
    if n-2==i:
        print(c)
