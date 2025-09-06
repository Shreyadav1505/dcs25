arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# arr = [1, 5, 3, 2, 4, 6]
# k = 3
# arr = [1, 2, 3, 4]
# k = 2
# arr = [7, 7, 7, 7]
# k = 1
res=[]
for i in range(len(arr)-k+1):
    max=0
    for j in range(i,i+k):
        if arr[j]>max:
            max=arr[j]
    res.append(max)
print(res)
