arr = [1, 2, 4, 5]
# arr = [2, 3, 4, 5]
# arr = [1, 2, 3, 4]
# arr = [1]
flag=0
n=len(arr)
for i in range(n):
    if arr[i] != i+1:
        flag=1
        break
if flag==1:
    print(i+1)
else:
    print(i+2)
