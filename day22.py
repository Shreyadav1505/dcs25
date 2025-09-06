# arr = [3, 1, 4, 4, 5, 2, 6, 1, 4]
# k = 2
# arr = [2, 3, 4, 2, 2, 5, 5]
# k = 2
# arr = [1, 1, 1, 1]
# k = 1
# arr = [10]
# k = 1
arr = [6, 6, 6, 6, 7, 7, 8, 8, 8]
k = 3
no=-1
# for i in range(len(arr)):
for i in arr:
    if arr.count(i)==k:
        no=i
print(no)
