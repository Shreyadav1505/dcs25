# arr = [1, 2, -3, 3, -1, 2]
# arr =  [4, -1, -3, 1, 2, -1]
# arr = [1, 2, 3, 4]
# arr = [0, 0, 0]
arr = [-3, 1, 2, -3, 4, 0]
n = len(arr)
result = []

for start in range(n):
    curr_sum = 0
    for end in range(start, n):
        curr_sum += arr[end]
        if curr_sum == 0:
            result.append((start, end))
print(result)
