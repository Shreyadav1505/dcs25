arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
#arr1 = [10, 12, 14]
#arr2 = [1, 3, 5]
#arr1 = [2, 3, 8]
#arr2 = [4, 6, 10]
#arr1 = [1]
#arr2 = [2]
#m = len(arr1)
#n = len(arr2)

def next_gap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)

gap = next_gap(m + n)
while gap > 0:
    i = 0
    j = gap

    while j < m + n:
        if i < m and j < m:
            if arr1[i] > arr1[j]:
                arr1[i], arr1[j] = arr1[j], arr1[i]

        elif i < m and j >= m:
            if arr1[i] > arr2[j - m]:
                arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

        else:
            if arr2[i - m] > arr2[j - m]:
                arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

        i += 1
        j += 1

    gap = next_gap(gap)
print(arr1)
print(arr2)
