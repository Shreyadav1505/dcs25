# arr = [16, 17, 4, 3, 5, 2]
arr = [1, 2, 3, 4, 0]
# arr =[7, 10, 4, 10, 6, 5, 2]
# arr =[5]
# arr =[100, 50, 20, 10]
# arr=  [1, 2, 3, ..., 1000000]
arr1=[]
for i in range(len(arr)):
    for j in range(len(arr)-1,i,-1):
        flag=0
        # print(i,j)
        if arr[i]>arr[j]:
            # print(arr[i],arr[j],"arrs")
            continue
        else:
            flag=1
            break
    if flag == 0:
        arr1.append(arr[i])
        # print("arr1", arr1)
print(arr1)
