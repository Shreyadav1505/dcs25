arr = [0, 1, 2, 1, 0, 2, 1, 0]
# arr = [2, 2, 2, 2]
# arr = [1, 1, 1, 1]
# arr = [0, 0, 0, 0]
# arr = [2, 0, 1]
# arr = []

low= 0
mid =0
high = len(arr) -1

while(mid<=high):
    if arr[mid] ==0:
        arr[low], arr[mid] = arr[mid], arr[low]
        # print(arr, "1",mid)
        low +=1
        mid+=1
    if arr[mid] ==1:
        # print(arr, "2",mid)
        mid+=1
    else:
        arr[mid], arr[high]= arr[high] ,arr[mid]
        # print(arr, "3",mid)
        high-=1
print(arr)
    
